txt = ""
cont = 0

def incrementarContador():
      global cont
      cont +=1
      return "%d" %cont  

class Nodo():
    pass

class null(Nodo):
    def __init__(self):
        self.type = 'void'

    def imprimir(self,ident):
        print (ident + "nodo nulo")

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id+"[label= "+"nodo_nulo"+"]"+"\n\t"

        return id 

class program(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        print (ident + "Nodo: "+self.name)  
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        return "digraph G {\n\t"+txt+"}"

class program_declaration_list(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)  
    def traducir(self):
        global txt
        id = incrementarContador()
        
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"
        return id
        

class program_declaration(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        print (ident + "Nodo: "+self.name)  
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        return id

class declaration_import(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)  
    def traducir(self):
        global txt
        id = incrementarContador()
        
        son1 = self.son1.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        
        return id

class declaration_function(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self,ident):
        self.son1.imprimir(ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)
        
        
        print (ident + "Nodo: "+self.name)  
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"
        txt += id +"->"+son3+"\n\t"

        return id

class declaration_statement(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        print (ident + "Nodo: "+self.name)                         
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        
        return id


class param_list(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)
    def traducir(self):
        global txt

        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"

        return id


class comma_var_type(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        
        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)
    def traducir(self):
        global txt

        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"

        return id


class var_type(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)


        print (ident + "Nodo: "+self.name)
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"

        return id

class assign_type(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" "+ident)
        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"

        return id 

class statement_list(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"

        return id 

class statement_list_statement(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        
        return id 



class statement_list_command(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):
        self.son1.imprimir(" "+ ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"

        return id 

class statement_var(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"

        return id 

class statement_var_declaration(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()
        
        son1 = self.son1.traducir()
        txt += id + "[label=" + self.name + "]"+"\n\t"
        txt += id + "->"+son1+"\n\t"
        return id 

class statement_var_assignment(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        
        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"
        txt += id +"->"+son3+"\n\t"

        return id 

class statement_return(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"

        return id 

class command_if(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"

        return id 
	
class command_if_else(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)

        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)    
        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"
        txt += id +"->"+son3+"\n\t"

        return id 

class statement_print(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        return id 

class command_while(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"
        return id 

class command_for(Nodo):
    def __init__(self,son1,son2,son3,son4,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self,ident):
        self.son1.imprimir(" "+ ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)

        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" "+ident)
        else:
            self.son3.imprimir(" "+ident)

        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" "+ident)
        else:
            self.son4.imprimir(" "+ident)        
        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        return id 

class statement_call(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"

        return id 

class expression_list(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):
        self.son1.imprimir(" "+ ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"
        return id 

class comma_expression(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"
        return id 

class expression(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)
        print (ident + "Nodo: "+self.name)
        
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"
        txt += id +"->"+son3+"\n\t"
        
        return id 

class datatype_expression(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()
        son1 = self.son1.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        
        return id 

class on_paren_expression(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        print (ident + "Nodo: "+self.name)

        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        return id 

class call_expression(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        self.son2.imprimir(" "+ident)
        self.son3.imprimir(" "+ident)
        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"
        txt += id +"->"+son3+"\n\t"
        return id 

class expression_array_access(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):
        self.son1.imprimir(" "+ ident)
        self.son2.imprimir(" "+ ident)
        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"
        return id 

class var_type_expression(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)
        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        return id  

class expression_uminus_minus(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self,ident):
        self.son1.imprimir(" "+ ident)
        self.son2.imprimir(" "+ ident)
        self.son3.imprimir(" "+ ident)
        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"
        txt += id +"->"+son3+"\n\t"
        return id  

class expression_uminus_plus(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self,ident):
        self.son1.imprimir(" "+ ident)
        self.son2.imprimir(" "+ ident)
        self.son3.imprimir(" "+ ident)
        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"
        txt += id +"->"+son3+"\n\t"
        return id  

class relop(Nodo):
    def __init__(self,son1,name):
        self.name = name
        self.son1 = son1

    def imprimir(self,ident):
        self.son1.imprimir(" "+ ident)
        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"

        return id 

class relop_number(Nodo):
    def __init__(self,son1,son2,son3,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self,ident):
        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" "+ident)
        else:
            self.son1.imprimir(" "+ident)

        self.son2.imprimir(" "+ ident)
        self.son3.imprimir(" "+ ident)
        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"
        txt += id +"->"+son3+"\n\t"
        return id  


class relop_binary(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)

        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"
        
        return id  


class relop_string(Nodo):
    def __init__(self,son1,son2,name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self,ident):
        self.son1.imprimir(" "+ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" "+ident)
        else:
            self.son2.imprimir(" "+ident)
        print (ident + "Nodo: "+self.name)
        
    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        txt += id +"[label= "+self.name+"]"+"\n\t"
        txt += id +"->"+son1+"\n\t"
        txt += id +"->"+son2+"\n\t"
        return id 


class Id(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self,ident):
        print (ident+ "ID: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label=" + self.name + "]"+"\n\t"

        return id

class Uminus(Nodo):
    def __init__(self, name):
        self.name = name
    
    def imprimir(self,ident):
        print (ident+ "UMINUS: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class Times(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self,ident):
        print (ident+ "TIMES: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class Divide(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self,ident):
        print (ident+ "DIVIDE: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class Minus(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self,ident):
        print (ident+ "MINUS: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label=" + self.name + "]"+"\n\t"

        return id

class Plus(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self,ident):
        print (ident+ "PLUS: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label=" + self.name + "]"+"\n\t"

        return id

class Less(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self,ident):
        print (ident+ "LESS: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label=" + self.name + "]"+"\n\t"

        return id

class Lessequal(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self,ident):
        print (ident+ "LESSEQUAL: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class Greater(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self,ident):
        print (ident+ "GREATER: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class GreaterEqual(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self,ident):
        print (ident+ "GREATEREQUAL: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class Isequal(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self,ident):
        print (ident+ "ISEQUAL: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class Notequal(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self,ident):
        print (ident+ "NOTEQUAL: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

class HEX(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self,ident):
        print (ident+ "HEX: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label=" + self.name + "]"+"\n\t"

        return id

class Integer(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self,ident):
        print (ident+ "INTEGER: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label=" + self.name + "]"+"\n\t"

        return id

class String(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self,ident):
        print (ident+ "STRING: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label=" + self.name + "]"+"\n\t"

        return id

class Float(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self,ident):
        print (ident+ "FLOAT: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label=" + self.name + "]"+"\n\t"

        return id

class Assign(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self,ident):
        print (ident+ "ASSIGN: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \""+self.name+"\"]"+"\n\t"

        return id

# class empty(nodo):

