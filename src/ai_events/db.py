import sqlite3, json
from pathlib import Path
from .models import Event

DB_PATH = Path.home() / ".ai-events" / "events.sqlite"

def ensure_db():
    """Create database and tables if they don't exist"""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as cx:
        cx.execute("""CREATE TABLE IF NOT EXISTS events(
          id TEXT PRIMARY KEY,
          data TEXT NOT NULL
        )""")
        cx.execute("""CREATE TABLE IF NOT EXISTS meta(
          k TEXT PRIMARY KEY, v TEXT
        )""")

def get_connection():
    return sqlite3.connect(DB_PATH)

def upsert_event(event: Event):
    """Insert or update an event in the database"""
    ensure_db()
    conn = get_connection()
    cursor = conn.cursor()
    
    # Check if this is a new event (first time we're seeing it)
    cursor.execute('SELECT data FROM events WHERE id = ?', (event.id,))
    existing = cursor.fetchone()
    
    if not existing and not event.first_discovered:
        # New event - set first_discovered timestamp
        from datetime import datetime
        event.first_discovered = datetime.utcnow().isoformat()
    elif existing:
        # Existing event - preserve the original first_discovered timestamp
        existing_data = json.loads(existing[0])
        if 'first_discovered' in existing_data and existing_data['first_discovered']:
            event.first_discovered = existing_data['first_discovered']
    
    # Convert event to dict for storage
    event_data = event.model_dump_json()
    
    cursor.execute('''
        INSERT OR REPLACE INTO events (id, data) VALUES (?, ?)
    ''', (event.id, event_data))
    
    conn.commit()
    conn.close()

def get_all_events() -> list[Event]:
    """Retrieve all events from the database"""
    ensure_db()
    out=[]
    with sqlite3.connect(DB_PATH) as cx:
        for (data,) in cx.execute("SELECT data FROM events"):
            out.append(Event.model_validate_json(data))
    return out

def save_meta(k:str, v:str):
    """Save metadata key-value pair"""
    ensure_db()
    with sqlite3.connect(DB_PATH) as cx:
        cx.execute("REPLACE INTO meta(k,v) VALUES(?,?)", (k,v))
        cx.commit()

def load_meta(k:str) -> str|None:
    """Load metadata value by key"""
    ensure_db()
    with sqlite3.connect(DB_PATH) as cx:
        cur = cx.execute("SELECT v FROM meta WHERE k=?", (k,))
        row = cur.fetchone()
        return row[0] if row else None
