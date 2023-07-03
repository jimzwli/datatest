def test():
    path = Path("x.sql")
    dataset = os.environ['xxx']
    with path.open('r') as query_file:
        query_text = query_file.read()
        query = query_text.replace(replace("<x>", str(x))    
        resp = [
          dict(
              v,
              #checked_at=now_isostring,
          ) for v in self._fetch_data(query, dataset)
        ]
