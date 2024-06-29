from Document import Document
from Group import Group
from Proprieties import Description
from Proprieties import Tag
from Proprieties import History

name = "Clausula Primeira"
priority = 8
tag = Tag("Processo Judicial tananan")
description = Description("O Documento diz respeito ao processo tananan da pessoa fulano e beltrano apesar do ciclano blablabla")
history = ["23/01/2019", "12/03/2023", "14/06/2024"]

doc = Document(name, priority, tag, description, history)
doc.view()
doc.addAlteration("29/06/2024")
doc.view()