using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using System.Collections.ObjectModel;
using task1.efcore.Models;
using task1.Services;

namespace task1.ViewModels;

public partial class UserViewModel : ViewModelBase
{
    private readonly UserService _service = new();

    public ObservableCollection<User> Users { get; } = new();

    public UserViewModel()
    {
        Load();
    }

    private void Load()
    {
        Users.Clear();
        foreach (var u in _service.GetAll())
            Users.Add(u);
    }

    [ObservableProperty]
    private string login;

    [ObservableProperty]
    private string password;

    [ObservableProperty]
    private User selectedUser;

    public bool CanSave => SelectedUser != null;

    partial void OnSelectedUserChanged(User value)
    {
        OnPropertyChanged(nameof(CanSave));
    }

    [RelayCommand]
    public void Create()
    {
        var user = new User
        {
            Login = Login,
            Password = Password
        };

        _service.Add(user);
        Load();

        Login = "";
        Password = "";
    }

    [RelayCommand]
    public void Delete(User user)
    {
        _service.Delete(user);
        Load();
    }

    [RelayCommand]
    public void Edit(User user)
    {
        SelectedUser = user;
        Login = user.Login;
        Password = user.Password;
    }

    [RelayCommand]
    public void Save()
    {
        if (SelectedUser == null)
            return;

        SelectedUser.Login = Login;
        SelectedUser.Password = Password;

        _service.Update(SelectedUser);
        Load();

        Login = "";
        Password = "";
        SelectedUser = null;
    }
}