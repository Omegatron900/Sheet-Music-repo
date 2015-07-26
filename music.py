import final_project

input_1 = raw_input("What is the name of the song you want to search? ")
input_2 = raw_input("Who is it by? ")

output = final_project.Music(input_1, input_2)
output.youtube_search()
#output.sheet_music()
