# run the file as `python ./pytransdec/actions_generator.py`
# to generate a new actions.py file out of VectorAction.ch

def translate(input_file, output_file):
	output_file.write(f'''class Actions:\n''')
	# current index in the array
	index=0
	# this lines will be placed inside of class's ToString method
	for line in input_file:
		# ignore empty lines
		if line=="":
			continue
		splitted=line.split(':')
		name=to_valid_python_identifier(splitted[0])
		# get count
		if len(splitted)>1:
			count=int(splitted[1])
		else:
			count=1
		output_file.write(field(name, index))
		index+=count
	output_file.write(field('COUNT', index))

def to_valid_python_identifier(name):
	# here all of the characters 
	# that can exist in channels names 
	# but can't exist in python identifiers 
	# must be replaced with spaces
	processed=name.replace('/', ' ')
	uppercase_words=[word.upper() for word in processed.split()]
	# join the words into one string using '_' character
	return '_'.join(uppercase_words)

def field(name, value):
	return f'    {name}={value}\n'

if __name__=="__main__":
	input_file = open('pytransdec/VectorAction.ch', 'r')
	output_file = open('pytransdec/actions.py', 'w')

	translate(input_file, output_file)

	input_file.close()
	output_file.close()