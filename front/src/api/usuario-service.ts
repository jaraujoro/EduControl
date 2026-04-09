import http from "../utils/http";

export const list_usuario = () => {
  return http.get("/user/list_usuario/");
};

export const login_usuario = (data:any) => {
  return http.post("/user/login_usuario/", data);
}