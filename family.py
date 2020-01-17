from random import randint
class Family:
    def __init__(self, last_name):
     #init vem sendo o construtor#   
        self._last_name = last_name
        self._name = ""
        self._age = 0
       #parametro privado porque tiene um _ ao inicio e terá um metodo espeficico para modificarla# 
        self._members = [{"id": 1, "name": "Fernanda", "lastname": "Sampaio", "age": 23}]


    def _generateId(self):
        return randint(0, 99)
     #vai gerar um random#


#Methods#
    def add_member(self, member):
        member = {
        "id": self._generateId(),
        "name": member._name,
        "lastname": member._last_name,
        "age": member._age
        } 

        self._members.append(member)
        return member   
        

    def delete_member(self, id):
        pass

    def update_member(self, id, member):
         obj = self.get_member(id)
         obj.update(member)
         return obj
           

    def get_member(self, id):
        member = list(filter(lambda member: member["id"] == id, self._members))
        return member[0];

    def get_all_members(self):
            return self._members