class Tokenize:
    
    def tokenize(str):
        tokens = []
        word = ''
        for c in str:
            if (c == ' ' or c == '.' or c == ','):
                if(c != ' '):
                    word += c
                if(word != ''):
                    tokens.append(word)
                word = ''
                continue
            else:
                word += c
        return tokens
    
    '''
    def cleanAuth(str):
        revStr = str[::-1]

        for i in range(0, len(revStr)):
            author = 'Bill Gates'
            return author
            #while (revStr[i] != '"'):
            #    author += revStr[i]
            # Authorless string
            #return revStr[:-i:-1]
            '''

