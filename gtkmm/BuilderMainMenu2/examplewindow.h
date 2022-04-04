#ifndef GTKMM_EXAMPLEWINDOW_H
#define GTKMM_EXAMPLEWINDOW_H

#include <gtkmm.h>

class ExampleWindow : public Gtk::Window
{
public:
	ExampleWindow();
	~ExampleWindow() = default;

protected:
	//Signal handlers:
	void on_button_quit();

	//Child widgets:
	Gtk::Box m_VBox;

	Gtk::Button m_Button_Quit;
	Glib::RefPtr<Gtk::Builder> builder_;
};

#endif //GTKMM_EXAMPLEWINDOW_H