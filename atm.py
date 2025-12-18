from abc import ABC,abstractmethod
class NoteDispenser(ABC):
    def set_next_chain(self,Dispenser):
        self._next_chain=Dispenser
    @abstractmethod
    def can_dispense(self):
        pass
    @abstractmethod
    def dispense(self):
        pass
    def __init__(self,num_notes,note_val):
        self.num_notes=num_notes
        self.note_val=note_val
    def print_notes(self):
        print(self.note_val,self.num_notes)
class NoteDispenser200(NoteDispenser):
    def __init__(self,num_notes,note_val):
        super().__init__(20,200)
    def can_dispense(self):
        pass
    def dispense(self):
        pass
    
class NoteDispenser100(NoteDispenser):
    def __init__(self,num_notes,note_val):
        super().__init__(num_notes,note_val)

    def can_dispense(self):
        pass
    def dispense(self):
        pass

class NoteDispenser50(NoteDispenser):
    def __init__(self,num_notes,note_val):
        super().__init__(20,50)
  
    def can_dispense(self):
        pass
    def dispense(self):
        pass

disp100=NoteDispenser100(20,100)
disp200=NoteDispenser200(20,200)
disp50=NoteDispenser50(10,50)
disp200.set_next_chain(disp100)
disp100.set_next_chain(disp50)
disp200._next_chain.print_notes()