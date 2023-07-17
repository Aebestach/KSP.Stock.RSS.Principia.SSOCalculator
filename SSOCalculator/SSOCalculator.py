import wx
import Counter
import ReadFile
import GenerateFile
import math

# Define a global variable to store the current language setting
_ = wx.GetTranslation

# Define a global variable to store the current language setting
current_language = wx.LANGUAGE_ENGLISH


class SunSyncOrbitCalculator(wx.Frame):
    def __init__(self, parent, title):
        super(SunSyncOrbitCalculator, self).__init__(parent, title=title, size=(455, 550),style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX)
        self.SetMaxSize((455, 550))
        self.SetMinSize((455, 550))

        self.InitUI()
        self.Centre()

    def InitUI(self):
        self.panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Set the language based on the system language
        system_language = wx.Locale(wx.LANGUAGE_DEFAULT).GetCanonicalName()
        print(system_language)
        if system_language == "zh_CN":
            current_language = wx.LANGUAGE_CHINESE_SIMPLIFIED
        else:
            current_language = wx.LANGUAGE_ENGLISH

        self.locale = wx.Locale(current_language)
        self.locale.AddCatalogLookupPathPrefix('language')

        if current_language == wx.LANGUAGE_ENGLISH:
            self.locale.AddCatalog('en')
        elif current_language == wx.LANGUAGE_CHINESE_SIMPLIFIED:
            self.locale.AddCatalog('zh_CN')

        # current_language = wx.LANGUAGE_ENGLISH
        # self.locale = wx.Locale(current_language)
        # self.locale.AddCatalogLookupPathPrefix('language')
        # self.locale.AddCatalog('en')
        #
        # # current_language = wx.LANGUAGE_CHINESE_SIMPLIFIED
        # # self.locale = wx.Locale(current_language)
        # # self.locale.AddCatalogLookupPathPrefix('language')
        # # self.locale.AddCatalog('zh_CN')


        # # Create a language selection menu
        # languages = [wx.LANGUAGE_ENGLISH, wx.LANGUAGE_CHINESE_SIMPLIFIED]
        # languageChoices = [wx.Locale.GetLanguageName(lang) for lang in languages]

        sizer = wx.GridBagSizer(10, 5)

        # sizer.Add(wx.StaticText(self.panel, label="Language"), pos=(0, 0), span=(1, 1),flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)
        # self.languageChoice = wx.Choice(self.panel, choices=languageChoices)
        # self.languageChoice.Bind(wx.EVT_CHOICE, self.OnLanguageChoice)
        # sizer.Add(self.languageChoice, pos=(0, 1), span=(1, 4), flag=wx.EXPAND)

        # Add two choice controls before the input label
        choice1Items = ["Stock", "RealSolarSystem"]
        self.choice2Items = ReadFile.ReadPlanetName()
        # self.choice2Items = {
        #     "Stock": ['Kerbin', 'Eve', 'Moho', 'Duna', 'Jool', 'Dres', 'Eeloo', 'Gilly', 'Mun', 'Minmus', 'Ike', 'Laythe', 'Vall', 'Tylo', 'Bop', 'Pol'],
        #     "RealSolarSystem": ['Jupiter', 'Saturn', 'Neptune', 'Uranus', 'Earth', 'Venus', 'Mars', 'Mercury', 'Ganymede', 'Titan', 'Callisto', 'Io', 'Moon', 'Europa', 'Triton', 'Eris', 'Pluto', 'Titania', 'Oberon', 'Rhea', 'Iapetus', 'Charon', 'Umbriel', 'Ariel', 'Dione', 'Ceres', 'Tethys', 'Vesta', 'Enceladus', 'Miranda', 'Mimas', 'Phobos', 'Deimos'],
        # }


        self.inputL1 = wx.StaticText(self.panel, label=_("System"))
        sizer.Add(self.inputL1, pos=(0, 0), span=(1, 1), flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)
        self.choice1 = wx.Choice(self.panel, choices=choice1Items)
        self.choice1.SetMinSize((150, -1))
        self.choice1.Bind(wx.EVT_CHOICE, self.UpdateChoice2)
        sizer.Add(self.choice1, pos=(0, 1), span=(1, 1), flag=wx.RIGHT)

        self.inputL2 = wx.StaticText(self.panel, label=_("Planet"))
        sizer.Add(self.inputL2, pos=(0, 2), span=(1, 1), flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)
        self.choice2 = wx.Choice(self.panel, choices=self.choice2Items[choice1Items[0]])
        self.choice2.SetMinSize((120, -1))
        sizer.Add(self.choice2, pos=(0, 3), span=(1, 1), flag=wx.RIGHT)
        self.choice2.Enable(False)

        self.inputLabel = wx.StaticText(self.panel,label=_("----------------Please Enter Orbit Parameters----------------"))
        sizer.Add(self.inputLabel, pos=(1, 0), span=(2, 4), flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)

        self.input1Label = wx.StaticText(self.panel, label=_("Altitude(m)"))
        sizer.Add(self.input1Label, pos=(3, 0), span=(1, 2), flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)
        self.input1 = wx.TextCtrl(self.panel)
        sizer.Add(self.input1, pos=(3, 2), span=(1, 2), flag=wx.EXPAND)

        self.input2Label = wx.StaticText(self.panel, label=_("Eccentricity"))
        sizer.Add(self.input2Label, pos=(4, 0), span=(1, 2), flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)
        self.input2 = wx.TextCtrl(self.panel)
        sizer.Add(self.input2, pos=(4, 2), span=(1, 2), flag=wx.EXPAND)

        self.input3Label = wx.StaticText(self.panel, label=_("j2"))
        sizer.Add(self.input3Label, pos=(5, 0), span=(1, 2), flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)
        self.input3 = wx.TextCtrl(self.panel)
        sizer.Add(self.input3, pos=(5, 2), span=(1, 2), flag=wx.EXPAND)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.calcButton = wx.Button(self.panel, label=_("Calculate"))
        self.calcButton.Bind(wx.EVT_BUTTON, self.OnCalcButtonClicked)
        hbox.Add(self.calcButton, flag=wx.RIGHT, border=15)

        self.GenerateButton = wx.Button(self.panel, label=_("Generate Configuration File"))
        self.GenerateButton.SetMinSize(wx.Size(225, -1))
        self.GenerateButton.Bind(wx.EVT_BUTTON, self.OnGenerateButtonClicked)
        hbox.Add(self.GenerateButton, flag=wx.RIGHT)

        self.ClearButton = wx.Button(self.panel, label=_("Clear"))
        self.ClearButton.Bind(wx.EVT_BUTTON, self.OnClearButtonClicked)
        hbox.Add(self.ClearButton, flag=wx.RIGHT)
        self.ClearButton.Enable(False)


        sizer.Add(hbox, pos=(6, 0), span=(2, 4), flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)
        self.GenerateButton.Enable(False)


        self.outputLabel = wx.StaticText(self.panel, label=_("Calculation Result"))
        sizer.Add(self.outputLabel, pos=(8, 0), span=(1, 4), flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL)

        self.outputText = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        sizer.Add(self.outputText, pos=(9, 0), span=(10, 4), flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP)

        self.UpdateUI()
        self.panel.SetSizer(sizer)  # Set the sizer to the panel

    # def OnLanguageChoice(self, e):
    #     system_language = wx.Locale(wx.LANGUAGE_DEFAULT).GetCanonicalName()
    #     if system_language == "zh_CN":
    #         self.languageChoice.SetSelection(1)
    #         self.OnLanguageChoice(None)
    #     else:
    #         self.languageChoice.SetSelection(0)
    #         self.OnLanguageChoice(None)
    #
    #     self.UpdateUI()

    def UpdateUI(self):

        self.inputL1.SetLabel(_("System"))
        self.inputL2.SetLabel(_("Planet"))
        self.inputLabel.SetLabel(_("----------------Please Enter Orbit Parameters----------------"))
        self.input1Label.SetLabel(_("Altitude(m)"))
        self.input2Label.SetLabel(_("Eccentricity"))
        self.input3Label.SetLabel(_("j2"))
        self.calcButton.SetLabel(_("Calculate"))
        self.GenerateButton.SetLabel(_("Generate Configuration File"))
        self.outputLabel.SetLabel(_("Calculation Result"))
        self.ClearButton.SetLabel(_("Clear"))

    def OnCalcButtonClicked(self, e):
        # Get input parameters
        input1 = self.input1.GetValue()
        input2 = self.input2.GetValue()
        choice1Selection = self.choice1.GetStringSelection()
        if choice1Selection == 'RealSolarSystem':
            input3 = 0
        else:
            input3 = self.input3.GetValue()
        choice2Selection = self.choice2.GetStringSelection()

        self.GenerateButton.Enable(False)


        # Display calculation results
        if choice1Selection == 'RealSolarSystem':
            # Call the sun synchronous orbit calculation program
            result1, result2, result3, result4 = Counter.calculate_sun_sync_orbit(choice1Selection, choice2Selection, input1, input2, input3)

            if math.isnan(float(result2)):
                self.outputText.AppendText(_('Input error, please re-enter!') + '\n\n')
                self.ClearButton.Enable(True)
            else:
                self.outputText.AppendText("--------------Satellite Orbital Parameters--------------" + '\n' + "Planet:" + '\t\t' + str(result1) + '\n' + "Altitude:" + '\t\t' + input1 + ' m\n' + "Inclination:" + '\t' + str(result2) + ' °\n' + "SMA:" + '\t\t' + str(result3) + ' m\n' + "Eccentricity:" + '\t' +str(result4) + '\n\n')
                self.ClearButton.Enable(True)
        else:
            # Call the sun synchronous orbit calculation program
            result1, result2, result3, result4, result5 = Counter.calculate_sun_sync_orbit(choice1Selection, choice2Selection, input1, input2, input3)

            if math.isnan(float(result2)):
                self.outputText.AppendText(_('Input error, please re-enter!') + '\n\n')
                self.ClearButton.Enable(True)
            else:
                self.GenerateButton.Enable(True)
                self.choice2.Enable(False)
                self.outputText.AppendText("--------------Satellite Orbital Parameters--------------" + '\n' + "Planet:" + '\t\t' + str(result1) + '\n' + "Altitude:" + '\t\t' + input1 + ' m\n' + "Inclination:" + '\t' + str(result2) + ' °\n' + "SMA:" + '\t\t' + str(result3) + ' m\n' + "Eccentricity:" + '\t' +str(result4) + '\n' + "C(2,0)(cos):" + '\t' + str(result5) + '\n\n')


    def OnGenerateButtonClicked(self, e):
        choice2Selection = self.choice2.GetStringSelection()
        input3 = self.input3.GetValue()

        GenerateFile.ReadPlanetName(choice2Selection, input3)
        self.outputText.AppendText("------------Config Generated Successfully------------\n\n")
        self.GenerateButton.Enable(False)
        self.choice2.Enable(True)
        self.ClearButton.Enable(True)


    def UpdateChoice2(self, e):
        self.choice2.Enable(True)
        choice1Selection = self.choice1.GetStringSelection()
        newChoice2Items = self.choice2Items[choice1Selection]
        self.choice2.SetItems(newChoice2Items)

        if choice1Selection == 'RealSolarSystem':
            self.input3.Disable()
            self.GenerateButton.Enable(False)
        else:
            self.input3.Enable()

    def OnClearButtonClicked(self, e):
        self.input1.SetLabel('')
        self.input2.SetLabel('')
        self.input3.SetLabel('')
        self.ClearButton.Enable(False)


if __name__ == '__main__':
    app = wx.App()

    SunSyncOrbitCalculator(None, title='Sun Synchronous Orbit Calculator').Show()
    app.MainLoop()
