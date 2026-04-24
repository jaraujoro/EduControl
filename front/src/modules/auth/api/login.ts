import http from "../../../api/http";

export const login_usuario = (data:any) => {
  return http.post("/user/login_usuario/", data);
}