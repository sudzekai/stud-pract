using Avalonia;
using Avalonia.Controls;
using Avalonia.Markup.Xaml;

namespace task1.Views;

public partial class HomeView : UserControl
{
    public HomeView()
    {
        InitializeComponent();
        DataContext = new task1.ViewModels.HomeViewModel();
    }
}