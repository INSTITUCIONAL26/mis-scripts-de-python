import * as v from "./validators";
export default v;

if ((require as any).main === module) {
  console.log("es_dni 12345678Z ->", v.es_dni("12345678Z"));
  console.log("es_email a@b.com ->", v.es_email("a@b.com"));
  console.log("es_fecha 31/12/2020 ->", v.es_fecha("31/12/2020"));
  console.log("es_numero \"5.5\" ->", v.es_numero("5.5"));
}
