import pracmln

# hasDestination(vessel, location!)
# hasType(vessel, type!)
# type = {Fishing, Cargo, Other}
# location = {Italy, Turkey, OtherD}
# //1.123 Fishing(x) => hasDestination(x, Italy)
# 1.3863 hasType(Marcel, Fishing) ^ hasDestination(Marcel, Italy)
# 1.7346 hasType(Marcel, Cargo) ^ hasDestination(Marcel, Turkey)
# 1.7346 hasType(Marcel, Fishing)^ hasDestination(Marcel, Turkey)


mln = pracmln.MLN(mlnfile='marcel2.mln', grammar='StandardGrammar', logic='FirstOrderLogic')
db = pracmln.Database(mln)
#db << 'foo(X)'
mrf = mln.ground(db)
#q = 'hasType(Marcel, Fishing) ^ hasDestination(Marcel, Italy), hasType(Marcel, Fishing) ^ hasDestination(Marcel, Turkey), hasType(Marcel, Cargo) ^ hasDestination(Marcel, Italy), hasType(Marcel, Cargo) ^ hasDestination(Marcel, Turkey), hasType(Marcel, Other) ^ hasDestination(Marcel, Italy), hasType(Marcel, Other) ^ hasDestination(Marcel, Turkey),hasType(Marcel, Fishing) ^ hasDestination(Marcel, OtherD),hasType(Marcel, Cargo) ^ hasDestination(Marcel, OtherD), hasType(Marcel, Other) ^ hasDestination(Marcel, OtherD)'
#q = 'Fishing(Marcel) ^ hasDestination(Marcel, Italy), Cargo(Marcel) ^ hasDestination(Marcel, Italy), Fishing(Marcel) ^ hasDestination(Marcel, Turkey), Cargo(Marcel) ^ hasDestination(Marcel, Turkey)'
qs = 'Fishing(Marcel) ^ hasDestination(Marcel, Italy),Cargo(Marcel) ^ hasDestination(Marcel, Italy) , Other(Marcel) ^ hasDestination(Marcel, Italy), Fishing(Marcel) ^ hasDestination(Marcel, Turkey),Cargo(Marcel) ^ hasDestination(Marcel, Turkey), Other(Marcel) ^ hasDestination(Marcel, Turkey), Fishing(Marcel) ^ hasDestination(Marcel, OtherD), Cargo(Marcel) ^ hasDestination(Marcel, OtherD), Other(Marcel) ^ hasDestination(Marcel, OtherD)'

result = pracmln.MLNQuery(queries = qs, method = 'EnumerationAsk', mln = mln, db = db).run()
result.write()