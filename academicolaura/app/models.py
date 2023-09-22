from django.db import models

class Ocupacao(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome}'
    
class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome}, {self.uf}'

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    pai = models.CharField(max_length=50)
    mae = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    datanasc = models.DateField(max_length=50)
    email = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade,
                               on_delete=models.CASCADE)
    ocupacao = models.ForeignKey(Ocupacao,
                               on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nome}, {self.pai}, {self.mae}, {self.cpf}, {self.datanasc}, {self.email}, {self.cidade}, {self.ocupacao}' 
    
class Instituicao(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome}, {self.site}, {self.telefone}'

class Area(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome}'
    
class Cursos(models.Model):
    nome = models.CharField(max_length=50)
    cargahoraria = models.CharField(max_length=50)
    duracaomeses = models.CharField(max_length=50)
    areadosaber = models.ForeignKey(Area,
                               on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao,
                               on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nome}, {self.cargahoraria}, {self.duracaomeses}, {self.areadosaber}, {self.instituicao}'
    
class Semestre(models.Model):
    periodoatual = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.periodoatual}'
        
class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    area = models.ForeignKey(Area,
                             on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}, {self.area}'
    
class Matriculas(models.Model):
    instituicao = models.ForeignKey(Instituicao,
                               on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos,
                               on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa,
                               on_delete=models.CASCADE)
    datainicio = models.DateField(max_length=50)
    datatermino = models.DateField(max_length=50)
    
    def __str__(self):
        return f'{self.instituicao}, {self.curso}, {self.pessoa}, {self.datainicio}, {self.datatermino}'
    
class TipoAvaliacao(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.tipo}'

class Avaliacoes(models.Model):
    descricao = models.CharField(max_length=200)
    curso = models.ForeignKey(Cursos,
                               on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina,
                               on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoAvaliacao,
                                      on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.descricao} {self.curso}, {self.disciplina}, {self.tipo}'
    
class Frequencia(models.Model):
    curso = models.ForeignKey(Cursos,
                               on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina,
                               on_delete=models.CASCADE)
    numerofaltas = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.curso}, {self.disciplina}, {self.numerofaltas}'
    
class Turma(models.Model):
    nome = models.CharField(max_length=50)
    turno = models.CharField(max_length=50)
    periodo = models.ForeignKey(Semestre,
                              on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}, {self.turno}, {self.periodo}'

class Advertencia(models.Model):
    descricao = models.CharField(max_length=200)
    data = models.DateField()
    curso = models.ForeignKey(Cursos,
                               on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina,
                               on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa,
                               on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.descricao}, {self.curso}, {self.disciplina}, {self.pessoa}'
    
class DisciplinaCurso(models.Model):
    disciplina = models.ForeignKey(Disciplina,
                               on_delete=models.CASCADE)
    cargahoraria = models.CharField(max_length=50)
    curso = models.ForeignKey(Cursos,
                               on_delete=models.CASCADE)
    
    periodo = models.ForeignKey(Semestre,
                               on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.disciplina}, {self.cargahoraria}, {self.curso}, {self.periodo}'
    

    
