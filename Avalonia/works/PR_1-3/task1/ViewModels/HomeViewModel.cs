using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using static System.Net.Mime.MediaTypeNames;

namespace task1.ViewModels;

public partial class HomeViewModel : ViewModelBase
{
    [ObservableProperty]
    private string text;

    [RelayCommand]
    public void ChangeText()
    {
        Text = "Новый текст";
    }
}