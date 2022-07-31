import dbus, dbus.mainloop.glib, sys
from tools.function import *


def on_property_changed(interface, changed, invalidated):
    if interface != 'org.bluez.MediaPlayer1':
        return
    for prop, value in changed.items():
        if prop == 'Status':
            print('Playback Status: {}'.format(value))
        elif prop == 'Track':
            print('Music Info:')
            for key in ('Title', 'Artist', 'Album'):
                print('   {}: {}'.format(key, value.get(key, '')))


def vol(fd, condition):
    if str.startswith('play'):
        player_iface.Play()
    elif str.startswith('pause'):
        player_iface.Pause()
    elif str.startswith('next'):
        player_iface.Next()
    elif str.startswith('prev'):
        player_iface.Previous()
    elif str.startswith('vol'):

        if vol not in range(0, 128):
            print('Possible Values: 0-127')
            return True

    return True


def music_widget(window, heigth, width):
    play = create_button(window, 'play', bg='gray', command=lambda: player_iface.Play(), width=2, height=2)
    pause =create_button(window, 'pause', bg='gray', command=lambda: player_iface.Pause(), width=2, height=2)
    next = create_button(window, 'next', bg='gray', command=lambda: player_iface.Next(), width=2, height=2)
    prev = create_button(window, 'prev', bg='gray', command=lambda: player_iface.Previous(), width=2, height=2)
    vol_prev = create_button(window, 'vol-', bg='gray',
                  command=lambda: transport_prop_iface.Set('org.bluez.MediaTransport1', 'Volume', dbus.UInt16(vol - 1)),
                  width=2, height=2)
    vol_next = create_button(window, 'vol+', bg='gray',
                  command=lambda: transport_prop_iface.Set('org.bluez.MediaTransport1', 'Volume', dbus.UInt16(vol + 1)),
                  width=2, height=2)

    play.place(x=width*(2/6), y=heigth/2)
    pause.place(x=width*(3/6), y=heigth/2)
    next.place(x=width*(4/6), y=heigth/2)
    prev.place(x=width*(1/6), y=heigth/2)
    vol_prev.place(x=width*(0/6), y=heigth/2)
    vol_next.place(x=width*(5/6), y=heigth/2)


if __name__ == '__main__':
    vol = 30
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()
    obj = bus.get_object('org.bluez', "/")
    mgr = dbus.Interface(obj, 'org.freedesktop.DBus.ObjectManager')
    player_iface = None
    transport_prop_iface = None
    for path, ifaces in mgr.GetManagedObjects().items():
        if 'org.bluez.MediaPlayer1' in ifaces:
            player_iface = dbus.Interface(
                bus.get_object('org.bluez', path),
                'org.bluez.MediaPlayer1')
        elif 'org.bluez.MediaTransport1' in ifaces:
            transport_prop_iface = dbus.Interface(
                bus.get_object('org.bluez', path),
                'org.freedesktop.DBus.Properties')
    if not player_iface:
        sys.exit('Error: Media Player not found.')
    if not transport_prop_iface:
        sys.exit('Error: DBus.Properties iface not found.')

    bus.add_signal_receiver(
        on_property_changed,
        bus_name='org.bluez',
        signal_name='PropertiesChanged',
        dbus_interface='org.freedesktop.DBus.Properties')
