from django.shortcuts import render

"""
You can use this to get a subset of your data out instead of using open refine or CTRL + Find

lives in your app
"""

import csv

from django.http import HttpResponse

#django generic class view 
from django.views.generic import ListView

#from treestone.tree.models import the model that you are using in model = MyModel
from treestone.tree.models import Stones

#what this tells Django is that 

#name this after whatever model you are mostly pulling from
class StonesListView(ListView):
    #change this based on what model you are interestsed in trees, stone, etc
    model = Stones

    def get_data(self):
      """
      Get data for MyModel as we see fit and pass it to a list of dictionaries
      for CSV Writer
      """
      # By default get_queryset() will get every instance of MyModel
      mymodels = self.get_queryset()
      # but we'll look at ways to filter it down later

      #making an array of dictionaries 
      dictionary_list = []
      for model in mymodels:
        model_dict = {}
        model_dict['name'] = model.name #if its just a simple attribute field
        model_dict['alternate_name'] = model.alternate_name
        # Here we're referencing a foreign key object and then its name
        #model_dict['bibliography'] = model_dict.bibliography.name
        # Here we're grabbing a Django managed m2m and th
        #model_dict['topics'] = [topic.name for topic
        #                        in ';'.join(model_dict.topics.all())
        # the syntax looks hairy but it isn't -- we're just telling python
        # to get all the related topics, and then make a list of their name
        # properties and join them with a semi-colon
        # psuedo code for getting through table data out
        #citations = StoneCitation.objects.filter(stone=stone)
        # model_dict['alternate_name_cite'] = citations.filter(column_name='alternate_name')[0].bibliography

        # now we append it to the list
        dictionary_list.append(model_dict)

      return dictionary_list
      #and that gets your data, you built the rows of your csv. 

    def render_to_response(self, context, **kwargs):

        # This boiler plate sets up the response and sets fields that tell
        # your browser this is a file, not a webpage.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="mymodel.csv"' #just change mymodel if you want to here

        # these need to match your dictionary above
        # if they don't python will complain
        headers = ['name', 'alternate_name']

        #you dont need to edit anything else in here  
        writer = csv.DictWriter(response, headers)
        writer.writeheader()
        rows = self.get_data()
        for row in rows:
            writer.writerow(row)

        return response 

"""
the query_set command is a way of getting what you want out of your models with a lot less pain, you can keep chaining them 

in the example on the git hub it had a model named topics, and it gets places in the topics object where the name is Foodbar. This will limit your models down to only those models for which that was true

The link djangos making queries: 
retreiving specific objects with filters
"""