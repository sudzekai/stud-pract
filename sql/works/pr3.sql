--
USE Market;

-- 5.1
SELECT * FROM Author;

-- 5.2
SELECT LastName, FirstName 
FROM Author 
LIMIT 3;

-- 5.3
SELECT DISTINCT Country 
FROM Author 
ORDER BY Country ASC;

-- 5.4
SELECT 
    BookId, 
    Title, 
    '5%' AS Discount, 
    Price * 0.95 AS DiscountedPrice 
FROM Book;

-- 5.5
SELECT *,
    CASE 
        WHEN Price < 100 THEN 'дешевые'
        WHEN Price >= 100 AND Price <= 1000 THEN 'средние'
        ELSE 'дорогие'
    END AS PriceCategory
FROM Book
ORDER BY Price DESC;

-- 5.6
SELECT Login, LastName, FirstName, Phone 
FROM Customer 
WHERE Phone IS NOT NULL;

-- 5.7
SELECT Title 
FROM Book 
WHERE Title LIKE '%компьютер%';

-- 5.8
SELECT 
    MIN(Price) AS MinPrice, 
    MAX(Price) AS MaxPrice, 
    AVG(Price) AS AvgPrice 
FROM Book;

-- 5.9
SELECT AuthorId, Title, COUNT(*) AS BookCount
FROM Book
GROUP BY AuthorId, Title;

-- 5.10 
SELECT Country, COUNT(*) AS AuthorCount
FROM Author
GROUP BY Country
HAVING COUNT(*) > 1;
