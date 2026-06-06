## Code to write the story in formated way
story = "A little seed lay quietly in the soil,dreaming of the sky With sunshine and rain, it grew into a tall, strong tree.Soon, birds built nests in its branches, and it became a home for many "
print(story)

formated_story = """A little seed lay quietly in the soil,dreaming of the sky With sunshine and rain,
it grew into a tall, strong tree.Soon, birds built nests in its branches, 
and it became a home for many """
print(formated_story)

formated_story = """{}.A little seed lay quietly in the soil,
{}.dreaming of the sky With sunshine and rain,
{}.it grew into a tall, strong tree.Soon, 
{}.birds built nests in its branches, 
{}.and it became a home for many """.format(1, 2, 3, 4, 5)
print(formated_story)


