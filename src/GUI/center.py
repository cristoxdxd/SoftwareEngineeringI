def center(windows):
    windows.update_idletasks() 
    width = windows.winfo_width() 
    frm_width = windows.winfo_rootx() - windows.winfo_x() 
    win_width = width + 2 * frm_width 
    height = windows.winfo_height() 
    titlebar_height = windows.winfo_rooty() - windows.winfo_y() 
    win_height = height + titlebar_height + frm_width 
    x = windows.winfo_screenwidth() // 2 - win_width // 2 
    y = windows.winfo_screenheight() // 2 - win_height // 2 
    windows.geometry('{}x{}+{}+{}'.format(width, height, x, y)) 
    windows.deiconify()