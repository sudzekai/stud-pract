using System.Collections.ObjectModel;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using task1.Models;

namespace task1.ViewModels;

public partial class UserListViewModel : ViewModelBase
{
    public ObservableCollection<User> Users { get; } = new();

    public UserListViewModel()
    {
        Users.Add(new User { Login = "user1", Password = "111" });
        Users.Add(new User { Login = "user2", Password = "222" });
        Users.Add(new User { Login = "user3", Password = "333" });
    }

    [RelayCommand]
    public void Delete(User user)
    {
        Users.Remove(user);
    }

    [ObservableProperty]
    private string login;

    [ObservableProperty]
    private string password;

    [RelayCommand]
    public void Add()
    {
        if (!string.IsNullOrWhiteSpace(Login) && !string.IsNullOrWhiteSpace(Password))
        {
            Users.Add(new User
            {
                Login = Login,
                Password = Password
            });
            Login = "";
            Password = "";
        }
    }
}