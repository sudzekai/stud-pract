using System.Collections.Generic;
using System.Linq;
using task1.efcore.Data;
using task1.efcore.Models;

namespace task1.Services;

public class UserService
{
    private readonly AppDbContext _db;

    public UserService()
    {
        _db = new AppDbContext();
        _db.Database.EnsureCreated();
    }

    public List<User> GetAll() => [.._db.Users];

    public void Add(User user)
    {
        _db.Users.Add(user);
        _db.SaveChanges();
    }

    public void Delete(User user)
    {
        _db.Users.Remove(user);
        _db.SaveChanges();
    }

    public void Update(User user)
    {
        _db.Users.Update(user);
        _db.SaveChanges();
    }
}