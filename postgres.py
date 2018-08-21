import psycopg2

conn = psycopg2.connect(host="127.0.0.1", database="analyze", user="postgres", password="xxx")

cur = conn.cursor()

cur.execute("""
select left(xzqhdm,%(length)s) as xzqhdm_x, count(*) as num
                          from whxx_ss
                          where xzqhdm like %(like)s
                          group by left(xzqhdm, %(length)s)
""", ({"length": 6, "like": "5223%"}))

# display the PostgreSQL database server version
print(cur.rowcount)
