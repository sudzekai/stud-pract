using Microsoft.EntityFrameworkCore;
using System;
using System.IO;
using task1.efcore.Models;

namespace task1.efcore.Data;

public class AppDbContext : DbContext
{
    public DbSet<User> Users { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        string dbPath = Path.Combine(Directory.GetCurrentDirectory(), "data.db");
        optionsBuilder.UseSqlite($"Data Source={dbPath}");
    }
}