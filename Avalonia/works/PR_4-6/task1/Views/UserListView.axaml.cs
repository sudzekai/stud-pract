using Avalonia;
using Avalonia.Controls;
using Avalonia.Markup.Xaml;

namespace task1.Views;

public partial class UserListView : UserControl
{
    public UserListView()
    {
        InitializeComponent();
        DataContext = new ViewModels.UserListViewModel();
    }
}