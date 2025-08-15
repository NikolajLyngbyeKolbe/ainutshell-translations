function hæv(beløb) {
  if (beløb > tilRådighed) {
    fail("Ups, det har du ikke penge nok til!")
  } else {
      tilRådighed = tilRådighed - beløb;
  }
}
