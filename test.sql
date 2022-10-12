SELECT * FROM Estate
WHERE EsateType='商铺';

SELECT * FROM Owner
WHERE PersonID IN
(
    SELECT PersonID FROM Registration 
    GROUP BY PersonID
    HAVING COUNT(*)>=2
);

SELECT * FROM Owner
WHERE PersonID IN
(
    SELECT Registration.PersonID FROM Owner,Registration,Estate
    WHERE Owner.PersonID=Registration.PersonID AND Estate.EstateID=Registration.EstateID 
    GROUP BY PersonID,EstateCity
    HAVING COUNT(*)>=2
);
/*
EID12834271451
EID13267367571
*/
SELECT EstateCity,SUM(PropertyArea) FROM `Estate`
GROUP BY EstateCity
ORDER BY EstateCity;

SELECT EstateCity,CONVERT(SUM(Price),DECIMAL(12,2)) FROM `Registration`,`Estate`
WHERE Estate.EstateID=Registration.EstateID
GROUP BY EstateCity
ORDER BY EstateCity;

CREATE VIEW Capitalist AS
SELECT Owner.PersonID,Name,Estate.EstateID,EstateName,EstateType,PropertyArea,EstateBuildName,EstateCity,PurchaseDate,Price From `Estate`,`Owner`,`Registration`
WHERE Estate.EstateID=Registration.EstateID AND Owner.PersonID=Registration.PersonID
ORDER BY PurchaseDate DESC;
Drop VIEW `Capitalist`;
CREATE VIEW Calc AS
SELECT EstateCity,COUNT(Estate.EstateID) AS '住宅销售套数',SUM(Price) FROM `Estate`,`Registration`
WHERE Estate.EstateID=Registration.EstateID
GROUP BY EstateCity
ORDER BY EstateCity ;
DROP VIEW `Calc`