# Written by Nick Welch in the years 2005-2008.  Author disclaims copyright.

from whimsy import util, props

class update_client_property:
    def __call__(self, signal):
        propname = signal.wm.dpy.get_atom_name(signal.ev.atom)
        if propname not in props.supported_props():
            return
        signal.wm.window_to_client(signal.win).update_prop(propname)

# todo: click focus handler & sloppy focus handler

#todo: circulate request
class configure_request_handler:
    def __call__(self, signal):
        client_or_win = signal.wm.window_to_client(signal.win) or signal.win
        if client_or_win is signal.win:
            print "configuring raw window: %r" % util.configure_request_changes(signal.ev)
        client_or_win.configure(**util.configure_request_changes(signal.ev))

class install_colormap:
    def __call__(self, signal):
        signal.ev.colormap.install_colormap()

