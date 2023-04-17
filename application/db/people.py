import psycopg2
with psycopg2.connect(database="db", user="postgres", password="mypassword") as conn:
    with conn.cursor() as cur:
def get_employees(conn, name, surname, email):
    cur = conn.cursor()
    cur.execute("""
    #anything
    """
    conn.commit()

get_employees()

if __name__=='__main__':
    get_employees()