import http from "../../../api/http";

export const list_rol = () => {
  return http.get("/rol/list_rol/");
};

export const list_rol_x_menu = (rol_id: number) => {
  return http.get(`/rol/list_rol_x_menu/${rol_id}/`);
};

export const save_rol = (data : any) => {
  return http.post("/rol/save_rol/", data);
};
