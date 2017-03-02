# -*- coding: utf-8 -*-

#Scoutクラスを作る。Scoutクラスは、インスタンス変数として、name（スカウト名, 文字列）, worker_type(雇用形態, 文字列), skills (要求スキル文字列のリスト)を持つ。これらの値をとって初期化するメソッド __init__を作れ。
#Scoutクラスに、そのScoutの候補者を保持するインスタンス変数candidatesを追加せよ。candidatesはPersonオブジェクトのリストである。Scoutクラスに、Personをcandidatesに追加するインスタンスメソッドadd_candidateを追加せよ
class Scout:
    def __init__(self, name, worker_type, skills):
        self.name = name
        self.worker_type = worker_type
        self.skills = skills
        self.candidates = []

    def add_skill(self, skill):
        if skill in self.skills:
            return
        else:
            return self.skills.append(skill)
    
    #Scoutクラスに、そのScoutの候補者を保持するインスタンス変数candidatesを追加せよ。candidatesはPersonオブジェクトのリストである。Scoutクラスに、Personをcandidatesに追加するインスタンスメソッドadd_candidateを追加せよ
    def add_candidate(self, person):
        if person in self.candidates:
            return
        else:
            return self.candidates.append(person)

    #Scoutクラスに、候補者の名前のリストを返すget_candidate_name_listを定義せよ。
    def get_candidate_name_list(self):
        return [candidate.name for candidate in self.candidates]

    #Scoutクラスに、skillsに定義されたスキルのいずれかをもっている候補者のリストを返すメソッド search_candidate_orを定義せよ。
    def search_candidate_or(self):
        candidates_or = [] 
        for candidate in self.candidates:
            skill_list = candidate.skills + self.skills
            if len(skill_list) > len(set(skill_list)):
                candidates_or.append(candidate.name)
        return candidates_or

    #Scoutクラスに、skillsに定義されたスキルすべてをもっている候補者のリストを返すメソッド search_candidate_andを定義せよ。
    def search_candidate_and(self):
        candidates_and = []
        for candidate in self.candidates:
            skills_set = candidate.skills + self.skills
            if len(set(skills_set)) == len(skills_set) - len(self.skills):
                candidates_and.append(candidate.name)
        return candidates_and


#Personクラスを作る。Personクラスは、インスタンス変数として、name（人名, 文字列）, skills (保持スキル文字列のリスト）を持つ。これらの値をとって初期化するメソッド __init__を作れ。
class Person:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills



