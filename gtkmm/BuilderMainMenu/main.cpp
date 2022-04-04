#include "examplewindow.h"
#include <gtkmm/application.h>
#include <iostream>

int main(int argc, char *argv[])
{
	auto app = Gtk::Application::create(argc, argv, "org.gtkmm.example");

	ExampleWindow window;
	app->signal_activate().connect([&app]() {
		// Connect the menu to the MenuButton m_gears.
		// (The connection between action and menu item is specified in gears_menu.ui.)
		try {
			auto menu_builder = Gtk::Builder::create_from_file("./menu.ui");
			auto menu = Glib::RefPtr<Gio::Menu>::cast_dynamic(menu_builder->get_object("appmenu"));
			if (!menu)
				throw std::runtime_error("No 'appmenu' object in menu.ui");

			app->set_menubar(menu);
			app->set_app_menu(menu);
		} catch (const Glib::FileError& e) {
			std::cerr << e.what() << std::endl;
		} catch (const Gtk::BuilderError& e) {
			std::cerr << e.what() << std::endl;
		}
	});

	//Shows the window and returns when it is closed.
	return app->run(window);
}