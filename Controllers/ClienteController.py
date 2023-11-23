import services.database as db;

def Incluir(cliente):
    count = db.cursor.execute("""
    INSERT INTO Cliente (Nome, Idade, Cargo) 
    VALUES (?,?,?)""",
    cliente.nome, cliente.idade, cliente.cargo).rowcount
    db.cnxn.commit()
