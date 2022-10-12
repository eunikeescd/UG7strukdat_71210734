


class StackList: 
    def __init__(self): 
        self.stack_data = list() 
    
    def push(self, new_data): 
        self.stack_data.append(new_data) 

    def top(self): 
        if len(self.stack_data) ==0: 
            return None 
        else: 
            return self.stack_data[-1] 
    
    def pop(self): 
        if len(self.stack_data) == 0: 
            return None 
        else: 
            pop_data = self.stack_data.pop() 
            return pop_data 
    
    def size(self): 
        return len(self.stack_data) 
        
class UndoRedo: 
    def __init__(self):
        self.mainStack = StackList() #stack ini sebagai tempat menyimpan data pertama kali 
        self.backupStack = StackList() #stack ini sebagai tempat menyimpan data yang di hapus 
 
    def write(self,data): 
        d = self.mainStack.push(data)
        print(data,"Berhasil Ditambahkan!")

    def undo(self): #Tuliskan Code Anda Disini 
        if self.mainStack.size()== 0:
            print("Perintah Undo Tidak Dapat Di Lakukan")
        else:
            c = self.mainStack.stack_data[-1]
            self.backupStack.push(c)
            self.mainStack.pop()
            for i in self.mainStack.stack_data: print(i,end=' ')
            print('')

    def redo(self): #Tuliskan Code Anda Disini 
        if self.backupStack.size()== 0:
            print("Perintah Redo Tidak Dapat Di Lakukan")
        else:
            a = self.backupStack.stack_data[-1]
            self.mainStack.push(a)
            self.backupStack.pop()
            for i in self.backupStack.stack_data: print(i,end=' ')
            print('')



    def printInfo(self): #Tuliskan Code Anda Disini  
        for i in self.mainStack.stack_data: 
            print(i,end=' ')



if __name__ == '__main__': 
    obj_undoredo = UndoRedo() 
    obj_undoredo.undo() #Test case Jika belum ada data yang ditambahkan 
    obj_undoredo.redo() #Test case jika belum ada data yang di undo 
    obj_undoredo.write('Pada Suatu Hari hiduplah seorang kakek-kakek') 
    obj_undoredo.write("Dia tinggal sebatang kara di pegunungan") 
    obj_undoredo.write("Dia kemudian turun gunung buat kuliah") 
    obj_undoredo.write("SEMESTER 5 BANYAK TUGASSSSSSS !!!") 
    obj_undoredo.printInfo() 
    obj_undoredo.undo() 
    obj_undoredo.undo() 
    obj_undoredo.undo() 
    obj_undoredo.undo() 
    obj_undoredo.redo() 
    obj_undoredo.redo() 
    obj_undoredo.redo()
