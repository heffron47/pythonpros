import wx
from wx.core import Panel


class MyForm(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 
                          "Perk Ordering System")
        

        
        

        self.panel_one = PanelOne(self)
        self.panel_two = PanelTwo(self)
        self.panel_three = PanelThree(self)

        self.panel_two.Hide()
        self.panel_three.Hide()
       

        

        

        
        
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.sizer.Add(self.panel_two, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        self.SetClientSize(600,800)
        self.MaxImageSize=500
        self.Image = wx.StaticBitmap(self, bitmap=wx.Bitmap(self.MaxImageSize, self.MaxImageSize))
        Img = wx.Image('app\MicrosoftTeams-image.png', wx.BITMAP_TYPE_ANY)
        Img = Img.Scale(200,200,quality=wx.IMAGE_QUALITY_HIGH)
        self.Image.SetBitmap(wx.Bitmap(Img))
        
        color = wx.Colour(234,218,244)
        self.SetBackgroundColour(color)
        self.Image.SetPosition((200, 0))
        self.Bind(wx.EVT_BUTTON, self.switchPanels)
        

    def switchPanels(self, event):
        
            self.panel_one.Hide()
      
            self.panel_two.Show()
            self.Layout()
    
    
        
        
        


class PanelOne(wx.Panel):
   
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        self.LoginTitle = wx.StaticText(self, label = "User Authentication",  pos = (185,220),size=wx.DefaultSize)
        self.Username = wx.StaticText(self, wx.ID_ANY, 'Username', pos = (235, 288) )
        self.inputUsername = wx.TextCtrl(self, wx.ID_ANY, pos = (235,305))
        self.Password = wx.StaticText(self, wx.ID_ANY, 'Password', pos = (235, 348) )
        self.inputPassword = wx.TextCtrl(self, wx.ID_ANY, pos = (235,367))
        self.submitBttn=wx.Button(self, label='Submit', pos= (250,500))
        font = wx.Font(20, family = wx.FONTFAMILY_DECORATIVE, style = wx.FONTSTYLE_SLANT, weight = wx.FONTWEIGHT_THIN, 
                      underline = True, faceName ="Montserrat", encoding = wx.FONTENCODING_DEFAULT)
        self.LoginTitle.SetFont(font)
        color = wx.Colour(234,218,244)
        self.LoginTitle.SetBackgroundColour(color)

        if self.IsShown:
           pass
        else:
            self.submitBttn.Hide()

    
class PanelTwo(wx.Panel):
    
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        
        wx.Panel.__init__(self, parent=parent)
        font = wx.Font(20, family = wx.FONTFAMILY_DEFAULT, style = 2, weight = 90, 
                      underline = True, faceName ="Montserrat", encoding = wx.FONTENCODING_DEFAULT)
        
        self.CustomerInfo = wx.StaticText(self, label ='Customer Information', pos =(175,220))
        self.CustomerInfo.SetFont(font)
        self.nowRadioBttn = wx.RadioButton(self, label = 'New', pos = (215, 270))
        self.retRadioBttn = wx.RadioButton(self, label = 'Returning', pos = (315, 270))
        self.firstName = wx.StaticText(self, label ='First Name', pos =(215,330))
        self.inputFN = wx.TextCtrl(self, wx.ID_ANY, pos = (215,350),size = wx.Size(180,-1))
        self.lastName = wx.StaticText(self, label ='Last Name', pos =(215,390))
        self.inputLN = wx.TextCtrl(self, wx.ID_ANY, pos = (215,410),size = wx.Size(180,-1))
        self.Email = wx.StaticText(self, label ='Email', pos =(215,450))
        self.inputEmail = wx.TextCtrl(self, wx.ID_ANY, pos = (215,470),size = wx.Size(180,-1))
        self.phoneNum = wx.StaticText(self, label ='Phone Number', pos =(215,510))
        self.inputPN = wx.TextCtrl(self, wx.ID_ANY, pos = (215,530),size = wx.Size(180,-1))
        self.continueBttn= wx.Button(self, label = 'Continue', pos = (325,580))
        self.backBttn= wx.Button(self, label = 'Back', pos = (210,580))

        
        def switchNext(self):
            PanelOne.Hide()
            PanelTwo.Hide()
            PanelThree.Show()
            
       
        
        self.continueBttn.Bind(wx.EVT_BUTTON, switchNext)



class PanelThree(wx.Panel):
    pass

     
        
      


   

if __name__ == '__main__':
    
    app = wx.App()
    ex = MyForm()
    ex.Show()
    app.MainLoop()