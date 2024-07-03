array = [0,0,0,0,0,0,0,0]
class hashMap(object):
    
    def Add(self, key_input,value_input):
            
            self.key_input = key_input
            self.value_input = value_input
            
            def hash_function(key_input, value_input):
                array[key_input%len(array)] = (key_input, value_input)
                
            hash_function(key_input, value_input)
            
    def Remove(self, key_input):
        array[key_input%len(array)] = 0
        
    def __getitem__(self, index):
        return array[index]
    
    def __repr__(self, index):
        return array
    
    def __str__(self):
        return str(array)
    
nova = hashMap()

nova.Add(9,"Value")
nova.Remove(4)

print(nova)
