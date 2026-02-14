class Validator:
    @staticmethod
    def validate_id(id_value):
        if not id_value or len(id_value.strip()) == 0:
            return False, "✖️ El ID no puede estar vacío"
        return True, ""
    
    @staticmethod
    def validate_name(name):
        if not name or len(name.strip()) == 0:
            return False, "✖️ El nombre no puede estar vacío"
        if len(name.strip()) < 2:
            return False, "El nombre debe tener al menos 2 caracteres"
        return True, ""

    @staticmethod
    def validate_int(value):
        try:
            number = int(value)
            if number < 0:
                return False, "✖️El valor no puede ser negativo"
            return True, ""
        except ValueError:
            return False, "⚙️Debe ingresar un número entero válido"

    @staticmethod
    def validate_float(value):
        try:
            number = float(value)
            if number < 0:
                return False, "✖️El valor no puede ser negativo"
            return True, ""
        except ValueError:
            return False, "Debe ingresar un número decimal válido"
