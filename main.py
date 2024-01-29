from fastapi import FastAPI
from supabase import create_client
from decouple import config

app = FastAPI()
url = config("SUPABASE_URL")
key = config("SUPABASE_KEY")

@app.get("/invoices")
async def root():
  supa = create_client(url, key)

  return supa.from_("invoices").select("*").execute()

@app.get("/customers")
async def root():
  supa = create_client(url, key)

  return supa.from_("customers").select("*").execute()