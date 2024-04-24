# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "d", lazy.spawn("rofi -show run"))
]



# Define colors schemes
cs_htb = {
    # HTB 
    "background": "#141d2b",
    "background-2": "#0b121f",
    "highlight": "#9eee00",
    "highlight-2": "#aa0000",    
}

cs_fallout = {
    "background": "#0066b1",
    "background-2": "#fff773",
    "highlight": "#001423",
    "highlight-2": "#aa0000",    
}
        


# Set scheme 
colors = cs_htb

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus=colors["highlight"], border_normal=colors["background-2"], border_width=1, margin=8),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(margin = 8)
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

def open_launcher():
    qtile.cmd_spawn("rofi -show")

def open_powermenu():
    qtile.cmd_spawn("power")


widget_defaults = dict(
    font="NotoSansM NFP ExtBd",
    fontsize=16,
    padding=3,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="~/Pictures/wallpaper.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
		#Left
                widget.TextBox(
                	padding=15, 
                	text="\uef72", 
                	font="0xProto Nerd Font Mono", 
                	fontsize=28, 
                	mouse_callbacks={"Button1": open_launcher}
                ),
                	
                widget.Sep(
                	linewidth=0, 
                	padding=10
                ),
                	
                widget.TextBox(
                	font="0xProto Nerd Font Mono", 
                	text="\ue0b6", 
                	padding=0, 
                	foreground=colors["background-2"], 
                	fontsize=28
                ),
                
                widget.GroupBox(
                	background=colors["background-2"], 
                	block_highlight_text_color=colors["highlight"], 
                	borderwidth=4, 
                	highlight_method='block', 
                	this_current_screen_border=colors["background-2"], 
                	other_screen_border=colors["background-2"], 
                	padding=5
                ),
                
                widget.TextBox(
                	font="0xProto Nerd Font Mono", 
                	text="\ue0b4", 
                	padding=0, 
                	foreground=colors["background-2"], 
                	fontsize=28
                ),

                widget.Prompt(
                    padding=20
                    ),

                widget.Spacer(),
                
                #Middel
		        widget.TextBox(
                	font="0xProto Nerd Font Mono", 
                	text="\ue0b6", 
                	padding=0, 
                	foreground=colors["background-2"], 
                	fontsize=28
                ),
                
                widget.Clock(
                	foreground=colors["highlight"],
                	background=colors["background-2"],
                ),
                
                widget.TextBox(
                	font="0xProto Nerd Font Mono", 
                	text="\ue0b4", 
                	padding=0, 
                	foreground=colors["background-2"], 
                	fontsize=28
                ),

                widget.Spacer(),


                #Right
                widget.TextBox(
                	font="0xProto Nerd Font Mono", 
                	text="\ue0b6", 
                	padding=0, 
                	foreground=colors["background-2"], 
                	fontsize=28
                ),


                widget.TextBox(
                	text="󰏖", 
                	background=colors["background-2"]
                ),
                
                widget.CheckUpdates(
                	distro="Ubuntu", 
                	no_update_string="0", 
                	display_format="{updates}", 
                	colour_have_updates=colors["highlight"], 
                	colour_no_updates=colors["highlight"], 
                	background=colors["background-2"]
                ),
                
                widget.Sep(
                	linewidth=0, 
                	padding=10, 
                	background=colors["background-2"]
                ),
                
                widget.TextBox(
                	text="", 
                	background=colors["background-2"],
                	padding=3,
                ),
                
                widget.Memory(
                	foreground=colors["highlight"], 
                	format="{MemUsed: .0f}{mm}", 
                	background=colors["background-2"]
                ),
                
                widget.Sep(
                	linewidth=0, 
                	padding=10, 
                	background=colors["background-2"]
                ),
                
                widget.TextBox(
                	text="", 
                	background=colors["background-2"],
                	padding=8,
                ),
                
                widget.CPU(
                	foreground=colors["highlight"], 
                	format="{load_percent}%", 
                	background=colors["background-2"]
                ),

                widget.TextBox(
                	font="0xProto Nerd Font Mono", 
                	text="\ue0b4", 
                	padding=0, 
                	foreground=colors["background-2"], 
                	fontsize=28
                ),


                widget.Sep(
                	linewidth=0, 
                	padding=20
                ),
            
                widget.TextBox(
                	font="0xProto Nerd Font Mono", 
                	text="\ue0b6", 
                	padding=0, 
                	foreground=colors["background-2"], 
                	fontsize=28
                ),

                widget.PulseVolume(
                	emoji=True,
                	fontsize=18, 
                	emoji_list=["","","","" ], 
                	step=5, 
                	background=colors["background-2"],
                ),

                widget.PulseVolume(
                	emoji=False,
                	fontsize=18, 
                	emoji_list=["","","","" ], 
                	step=5, 
                	background=colors["background-2"],
                    foreground=colors["highlight"]
                ),

                widget.TextBox(
                	font="0xProto Nerd Font Mono", 
                	text="\ue0b4", 
                	padding=0, 
                	foreground=colors["background-2"], 
                	fontsize=28,
                ),

                widget.Sep(
                	linewidth=0, 
                	padding=10,
                ),
                
                widget.TextBox(
                	font="0xProto Nerd Font Mono", 
                	text="\ue0b6", 
                	padding=0, 
                	foreground=colors["background-2"], 
                	fontsize=28
                ),

                widget.TextBox(
                	text="󰖂",
                	fontsize=18,  
                	background=colors["background-2"],
                ),

                widget.Sep(
                	linewidth=0, 
                	padding=10,
                	background=colors["background-2"]
                ),
                widget.TextBox(
                	text="",
                	fontsize=18, 
                	padding=15, 
                	background=colors["background-2"],
                ),

                widget.Sep(
                	linewidth=0, 
                	padding=10,
                	background=colors["background-2"]
                ),
                                
                widget.TextBox(
                	text="\uf011", 
                	fontsize=18,  
                	foreground=colors["highlight-2"], 
                	background=colors["background-2"],
                	mouse_callbacks={"Button1": open_powermenu}
                ),
                   
            
                widget.TextBox(
                	font="0xProto Nerd Font Mono", 
                	text="\ue0b4", 
                	padding=0, 
                	foreground=colors["background-2"], 
                	fontsize=28,
                ),

            ],
            
            32,
            background=colors["background"],  # Set the background color of the bar
            foreground=colors["highlight"],  # Set the foreground color of the bar
            border_color=[colors["background"], colors["background"], colors["background"], colors["background"]],
            border_width=[4, 4, 4, 4],
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,i
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
