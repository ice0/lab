#include <iostream>
#include "examplewindow.h"

ExampleWindow::ExampleWindow()
		: m_VBox(Gtk::ORIENTATION_VERTICAL),
		  m_Button_Quit("Quit")
{
	set_title("Gtk::TreeView Editable Cells example");
	set_border_width(5);
	set_default_size(400, 200);

	add(m_VBox);
	m_VBox.add(m_Button_Quit);
	m_Button_Quit.signal_clicked().connect([this]() {
		on_button_quit();
	});
	show_all();
}

void ExampleWindow::on_button_quit()
{
	std::cout << "Hello: " << std::endl;
}
