Persons = {
    'Tom':{
        'Hobby':"basketball",
         'Location':"BeiJing",
         'Gender':"male",
         },
    'Jerry':{
         'Hobby':"pc_games",
         'Location':"ShangHai",
         'Gender':"male",
         },
    'LYM':{
         'Hobby':"football",
         'Location':"NanJing",
         'Gender':"female",
         },
}

Persons['wsc'] =  {
    'Hobby':'me',
    'Location':'my home',
    'Gender':'female',
    }

del Persons['Tom'];

Persons['Biu'] = Persons.pop('wsc');
Persons['Jerry']['Hobby'] = 'Games';
for person,person_info in Persons.items():
   print("\nI know something about you, " + person);
   hobby = person_info['Hobby'];
   location = person_info['Location'];
   Gender = person_info['Gender'];
   print("You like " + hobby.title());
   print("You live in " + location.title());
   if Gender == 'female':
       print("I also predict that you will love me.");
 
print("HEllo");
