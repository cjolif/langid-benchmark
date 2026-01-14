# https://gist.github.com/carlopires/1262033/c52ef0f7ce4f58108619508308372edd8d0bd518
iso_639_choices = [
('en', 'English'),
('fr', 'French'),
('de', 'German'),
('it', 'Italian'),
('es', 'Spanish; Castilian'),
]

lang_dict = dict()
for choices in iso_639_choices:
  for l in choices[1].split("; "):
    lang_dict[l] = choices[0]