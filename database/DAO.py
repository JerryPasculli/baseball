from database.DB_connect import DBConnect
from model.sqaudra import Squadra


class DAO():
    def __init__(self):
        pass



    @staticmethod
    def getSquadre(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True
        )
        query = """select ID, teamCode, name, year
from teams t where year = %s"""
        cursor.execute(query, [anno])
        lista = []
        for element in cursor:
            squadra = Squadra(**element)
            lista.append(squadra)
        conn.close()
        cursor.close()
        return lista


    @staticmethod
    def getArchi(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(
        )
        query = """with teamsVeri as (select ID, teamCode, name, year
from teams t where year = %s),
pesi as (
select t.ID, sum(salary) as somma
from appearances a, salaries s, teamsVeri t
where t.ID = a.teamID and s.playerID = a.playerID and s.year = %s and a.year = %s
group by t.ID)

select t1.ID, t2.ID, sum(somma)
from teamsVeri t1, teamsVeri t2, pesi p
where t1.ID>t2.ID and (p.ID = t1.ID or p.ID = t2.ID)
group by t1.ID, t2.ID"""
        cursor.execute(query, [anno, anno, anno])
        lista = []
        for element in cursor:
            lista.append(element)
        conn.close()
        cursor.close()
        return lista

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(
        )
        query = """select distinct year
        from teams"""
        cursor.execute(query)
        lista = []
        for element in cursor:
            lista.append(element)
        conn.close()
        cursor.close()
        return lista

