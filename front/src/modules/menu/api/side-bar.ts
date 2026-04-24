import http from "../../../api/http";

export const list_menu = () => {
    return http.get("/menu/list_menu_x_usuario/");
}