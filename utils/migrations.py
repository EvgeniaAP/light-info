from utils.models import Figure, Formula, Feature, Theorema


class Migrations:

    # знак умножения \\times
    # степень ^{}
    # корень \\sqrt{} | а так \\sqrt[3]{} -> кубический корень и любой другой по аналогии
    # дробь \\frac{n}{x} -> выглядит как 1/2
    def latex_formula(self, formula: str) -> str:
        return '\\documentclass[14pt]{book} \\begin{document} $ ' + formula + ' $ \\end{document}'

    def load_v1(self, app, db):
        print("BD load start")

        items = []

        # Куб

        formula_p_cube = Formula(name='Периметр куба', description='', latex=self.latex_formula('P = 12 a'))
        items.append(formula_p_cube)

        formula_s_cube = Formula(name='Площадь куба', description='', latex=self.latex_formula('S = 6 a^2'))
        items.append(formula_s_cube)

        formula_v_cube = Formula(name='Объём куба', description='', latex=self.latex_formula('V = a^{3}'))
        items.append(formula_v_cube)

        cube_feat_1 = Feature(
            text='Четыре сечения куба являются правильными шестиугольниками — эти сечения проходят через центр куба перпендикулярно четырём его главным диагоналям.')
        items.append(cube_feat_1)

        cube_feat_2 = Feature(
            text='В куб можно вписать тетраэдр двумя способами. В обоих случаях четыре вершины тетраэдра будут совмещены с четырьмя вершинами куба и все шесть рёбер тетраэдра будут принадлежать граням куба. В первом случае все вершины тетраэдра принадлежат граням трёхгранного угла, вершина которого совпадает с одной из вершин куба. Во втором случае попарно скрещивающиеся ребра тетраэдра принадлежат попарно противолежащим граням куба. Такой тетраэдр является правильным, а его объём составляет 1/3 от объёма куба.')
        items.append(cube_feat_2)

        cube_feat_3 = Feature(
            text='В куб можно вписать октаэдр, притом все шесть вершин октаэдра будут совмещены с центрами шести граней куба.')
        items.append(cube_feat_3)

        cube_feat_4 = Feature(
            text='Куб можно вписать в октаэдр, притом все восемь вершин куба будут расположены в центрах восьми граней октаэдра.')
        items.append(cube_feat_4)

        cube_feat_5 = Feature(
            text='В куб можно вписать икосаэдр, при этом шесть взаимно параллельных рёбер икосаэдра будут расположены соответственно на шести гранях куба, остальные 24 ребра — внутри куба. Все двенадцать вершин икосаэдра будут лежать на шести гранях куба.')
        items.append(cube_feat_5)

        formula_d_of_cube = Formula(name='Длина диагонали куба', description='',
                                    latex=self.latex_formula('d = a\\sqrt{3}'))
        items.append(formula_d_of_cube)

        cube_feat_6 = Feature(
            text='Диагональю куба называют отрезок, соединяющий две вершины, симметричные относительно центра куба.',
            formula=formula_d_of_cube)
        items.append(cube_feat_6)

        cube = Figure(name='Куб',
                      info='Куб — многогранник, поверхность которого состоит из шести квадратов. Куб является правильным многогранником. Частный случай параллелепипеда и призмы.',
                      image='cube',
                      plain=False,
                      features=[cube_feat_1, cube_feat_2, cube_feat_3, cube_feat_4, cube_feat_5, cube_feat_6])
        items.append(cube)

        # Квадрат

        formula_s_sqares = Formula(name='Площадь квадрата', description='', latex=self.latex_formula('S = a^{2} = 2 R^{2} = 4 r^2 = \\frac{1}{2} d^2'))
        items.append(formula_s_sqares)

        formula_p_sqares = Formula(name='Периметр квадрата', description='',
                                   latex=self.latex_formula('S = 4 a = 4 \\sqrt{2} R = 8 r'))
        items.append(formula_p_sqares)

        formula_d_of_sqare = Formula(name='Длина диагонали квадрата', description='',
                                     latex=self.latex_formula('d = a \\sqrt{2}'))
        items.append(formula_d_of_sqare)

        sqare_feat_1 = Feature(text='Диагонали квадрата равны, взаимно перпендикулярны, делятся точкой пересечения пополам и сами делят углы квадрата пополам (другими словами, являются биссектрисами внутренних углов квадрата).',
                               formula=formula_d_of_sqare)
        items.append(sqare_feat_1)


        sqare = Figure(name='Квадрат',
                       info='Квадрат — правильный четырёхугольник, то есть плоский четырёхугольник, у которого все углы и все стороны равны. Каждый угол квадрата — прямой (90 град.).',
                       image='https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/SquareDefinition.svg/200px-SquareDefinition.png',
                       plain=True,
                       features=[sqare_feat_1])
        items.append(sqare)

        # Теорема Пифагора

        formula_pifa = Formula(name='Формула Пифагора', description='', latex=self.latex_formula('c^2 = a^2 + b^2'))
        items.append(formula_pifa)

        theorema = Theorema(name='Теорема Пифагора', text='Теоре́ма Пифаго́ра — одна из основополагающих теорем евклидовой геометрии, устанавливающая соотношение между сторонами прямоугольного треугольника: сумма квадратов длин катетов равна квадрату длины гипотенузы. Основные направления доказательств: алгебраическое использование соотношений элементов треугольника (таков, например, популярный метод подобия), метод площадей, существуют также различные экзотические доказательства (например, с помощью дифференциальных уравнений).', formulas=[formula_pifa])
        items.append(theorema)

        print("BD load finish")
        return items
