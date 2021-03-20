import json
import rpyc
from rpyc.utils.server import ThreadedServer

PORT = 12345

class MyDatabase:
	def __init__(self, filePath):
		self._filePath = filePath
		self._inMemory = []
		self._load()

	def _save(self):
		with open(self._filePath, 'w') as f:
			json.dump(self._inMemory, f)

	def _load(self):
		try:
			with open(self._filePath, 'r') as f:
				self._inMemory = json.load(f)
		except FileNotFoundError:
			print('database file not found, creating file')
			self._save()

	def insert(self, obj):
		self._inMemory.append(obj)
		self._save()

	def update(self, filter_obj, newObj):
		for i in range(len(self._inMemory)):
			obj = self._inMemory[i]
			match = False
			for key in filter_obj:
				match = (key in obj) and (obj[key] == filter_obj[key])
				if not match: break
		
			if match:
				self._inMemory[i] = newObj
				break

	def get_all(self):
		return self._inMemory.copy()
		
	def filter(self, filter_obj):
		filtered = []
		for obj in self._inMemory:
			match = False
			for key in filter_obj:
				match = (key in obj) and (obj[key] == filter_obj[key])
				if not match: break
		
			if match: filtered.append(obj)

		return filtered


class MyService(rpyc.Service):
	def __init__(self):
		self._db = MyDatabase('notas.json')

	def exposed_cadastrar_nota(self, mat, cod_disc, nota):
		filter_grade = { 'mat': mat, 'cod_disc': cod_disc }
		new_grade = { 'mat': mat, 'cod_disc': cod_disc, 'nota': nota }
		grades = self._db.filter(filter_grade)
		if len(grades) > 0:
			self._db.update(filter_grade, new_grade)
			print('nota sobreescrita')
		else:
			self._db.insert(new_grade)
			print('nota inserida')

	def exposed_consultar_nota(self, mat, cod_disc):
		grades = self._db.filter({ 'mat': mat, 'cod_disc': cod_disc })
		if len(grades) > 0:
			return grades[0]['nota']

		return f'Não existe nota para o aluno de matricula {mat} na disciplina {cod_disc}'

	def exposed_consultar_notas(self, mat):
		grades = self._db.filter({'mat': mat})
		if len(grades) > 0:
			return grades

		return f'Não existem notas para o aluno de matricula {mat}'

	def exposed_consultar_cr(self, mat):
		grades = self._db.filter({'mat': mat})
		if len(grades) > 0:
			avg = 0
			for grade in grades:
				avg += grade['nota']
			return avg / len(grades)

		return f'Não existem notas para o aluno de matricula {mat}'

if __name__ == "__main__":
	server = ThreadedServer(MyService, port = PORT)
	print("servidor ouvindo na porta", PORT)
	server.start()
