graph G {
  ga1 -- ga4
  ga0 -- ga5
  ga1 -- ga5
  ga0 -- ga1
  ga0 -- ga2
  ga1 -- ga2
  ga0 [label="Cargo(Marcel)"]
  ga1 [label="Fishing(Marcel)"]
  ga2 [label="Other(Marcel)"]
  ga3 [label="hasDestination(Marcel,OtherD)"]
  ga4 [label="hasDestination(Marcel,Italy)"]
  ga5 [label="hasDestination(Marcel,Turkey)"]
}
