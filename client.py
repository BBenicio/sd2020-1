import rpyc

conn = rpyc.connect("localhost", 12345)

conn.root.cadastrar_nota(1, 1, 10)
conn.root.cadastrar_nota(1, 2, 8)
conn.root.cadastrar_nota(1, 3, 8)
conn.root.cadastrar_nota(1, 4, 10)

conn.root.cadastrar_nota(2, 1, 10)
conn.root.cadastrar_nota(2, 2, 8)

conn.root.cadastrar_nota(3, 2, 0)

print(conn.root.consultar_nota(1, 2))
print(conn.root.consultar_nota(3, 1))

print(conn.root.consultar_notas(1))

print(conn.root.consultar_cr(2))