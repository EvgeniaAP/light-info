from utils.models import Figure, Formula, Feature, Theorema


class Migrations:

    # знак умножения \\times
    # степень ^{}
    # корень \\sqrt{} | а так \\sqrt[3]{} -> кубический корень и любой другой по аналогии
    # дробь \\frac{n}{x} -> выглядит как n/x
    def latex_formula(self, formula: str) -> str:
        return '\\documentclass[14pt]{book} \\begin{document} $ ' + formula + ' $ \\end{document}'

    def load_v1(self, app, db):
        print("BD load start")

        items = []

        # Куб

        formula_p_cube = Formula(name='Периметр куба', description='Для того что бы вычислить периметр куба необходимо знать длину его ребра, как известно у куба 12 ребер . Если нам известна указанная величина, для нас не составит труда вычислить периметр.Периметр куба рассчитывается по следующей формуле.Где P – периметр, a – длина ребра куба.', latex=self.latex_formula('P = 12 a'))
        items.append(formula_p_cube)

        formula_s_cube = Formula(name='Площадь куба', description='Площадь (S) поверхности куба равна произведению числа 6 на длину его ребра в квадрате.', latex=self.latex_formula('S = 6 a^2'))
        items.append(formula_s_cube)

        formula_v_cube = Formula(name='Объём куба', description='Объем куба рассчитывается путем умножения длины, ширины и высоты куба. Для куба длина, ширина и высота равны. ', latex=self.latex_formula('V = a^{3}'))
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

        formula_d_of_cube = Formula(name='Длина диагонали куба', description='Диагональ куба – это расстояние между двумя противоположными углами, проходящее через центр куба. Другими словами, это длина линии, соединяющей два самых удаленных друг от друга угла. Формула диагонали куба. Формула для вычисления диагонали куба проста. Вы просто умножаете длину одного ребра на квадратный корень из трех.',
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

        formula_s_sqares = Formula(name='Площадь квадрата', description='Для вычисления площади квадрата нужно умножить его длину на саму себя', latex=self.latex_formula('S = a^{2} = 2 R^{2} = 4 r^2 = \\frac{1}{2} d^2'))
        items.append(formula_s_sqares)

        formula_p_sqares = Formula(name='Периметр квадрата', description='Периметр квадрата – это сумма длин всех его сторон. Чтобы посчитать периметр квадрата, можно сложить длины всех сторон, либо умножить длину одной его стороны на четыре.',
                                   latex=self.latex_formula('S = 4 a = 4 \\sqrt{2} R = 8 r'))
        items.append(formula_p_sqares)

        formula_d_of_sqare = Formula(name='Длина диагонали квадрата', description='Диагональ квадрата — это любой отрезок, соединяющий две вершины противоположных углов квадрата.Диагональ любого квадрата всегда больше его стороны в√2 раз.',
                                     latex=self.latex_formula('d = a \\sqrt{2}'))
        items.append(formula_d_of_sqare)

        sqare_feat_1 = Feature(text='Диагонали квадрата равны, взаимно перпендикулярны, делятся точкой пересечения пополам и сами делят углы квадрата пополам (другими словами, являются биссектрисами внутренних углов квадрата).',
                               formula=formula_d_of_sqare)
        items.append(sqare_feat_1)
        sqare_feat_2 = Feature(text='Все углы квадрата — прямые, все стороны квадрата — равны.')
        items.append(sqare_feat_2)
        sqare_feat_3 = Feature(text='Диагонали квадрата делят его на 4 равных прямоугольных равнобедренных треугольника')
        items.append(sqare_feat_3)


        sqare = Figure(name='Квадрат',
                       info='Квадрат — правильный четырёхугольник, то есть плоский четырёхугольник, у которого все углы и все стороны равны. Каждый угол квадрата — прямой (90 град.). Квадрат будет квадратом, если выполняется хотя бы одно из следующих условий: \n 1. Все стороны равны и между внутренними углами есть прямой угол. \n 2. Диагонали равны, перпендикулярны и, пересекаясь, делятся пополам. \n 3. Квадрат обладает вращательной симметрией: он не изменится при повороте на 90˚.',
                       image='https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/SquareDefinition.svg/200px-SquareDefinition.png',
                       plain=True,
                       features=[sqare_feat_1,sqare_feat_2,sqare_feat_3])
        items.append(sqare)

        #Параллелограмм
        formula_s_parallelogram = Formula(name='Площадь параллелограмма', description='Параллелограмм — это четырехугольник, у которого противолежащие стороны попарно параллельны. Площадь параллелограмма — часть плоскости, ограниченная данной фигурой.',
                                   latex=self.latex_formula('S = h a'))
        items.append(formula_s_parallelogram)
        formula_p_parallelogram = Formula(name='Пeриметр параллелограмма', description='Периметром параллелограмма называется сумма длин всех сторон параллелограмма.',
                                          latex=self.latex_formula('P = 2 (a + b)'))
        items.append(formula_p_parallelogram)
        parallelogram_feat_1 = Feature(text='Противоположные стороны параллелограмма равны.ABCD — параллелограмм, значит, AB = DC, BC = AD.')
        items.append(parallelogram_feat_1)
        parallelogram_feat_2 = Feature(text='Противоположные углы параллелограмма равны.')
        items.append(parallelogram_feat_2)
        parallelogram_feat_3 = Feature(text='Диагонали параллелограмма точкой пересечения делятся пополам')
        items.append(parallelogram_feat_3)
        parallelogram_feat_4 = Feature(text='Диагональ делит параллелограмм на два равных треугольника.')
        items.append(parallelogram_feat_4)
        parallelogram_feat_5 = Feature(text='Сумма углов в параллелограмме, прилежащих к одной стороне, равна 180 градусам.')
        items.append(parallelogram_feat_5)
        parallelogram = Figure(name='Параллелограмм',
                               info='Параллелограмм — это четырехугольник, у которого противоположные стороны попарно параллельны и равны.Признаки параллелограмма: \n 1— две противолежащие стороны равны и параллельны, \n 2— противолежащие стороны попарно равны, \n 3— диагонали пересекаются и точкой пересечения делятся пополам, \n 4— каждая диагональ делит четырехугольник на два равных треугольника.',
                               image='https://fs.znanio.ru/8c0997/b7/85/099a8aa13dcd54d380efa3490d3226cfd8.png',
                               plain=True,
                               features=[parallelogram_feat_1,parallelogram_feat_2,parallelogram_feat_3,parallelogram_feat_4,parallelogram_feat_5])
        items.append(parallelogram)
        #Прямоугольник
        formula_p_rectangle = Formula(name='Периметр прямоугольника', description='Периметр (P) любого треугольника равен сумме длин всех его сторон.',
                                      latex=self.latex_formula('P = 2 (a + b)'))
        items.append(formula_p_rectangle)
        formula_s_rectangle = Formula(name='Площадь прямоугольника', description='Площадь треугольника – численная характеристика, из которой мы узнаем о размере части плоскости, ограниченной данной фигурой.',
                                      latex=self.latex_formula('S = a b'))
        items.append(formula_s_rectangle)
        rectangle_feat_1 = Feature(text='Противоположные стороны попарно равны и параллельны.')
        items.append(rectangle_feat_1)
        rectangle_feat_2 = Feature(text='Противоположные углы равны.')
        items.append(rectangle_feat_2)
        rectangle_feat_3 = Feature(text='Все углы равны 90 градусам, что вытекает из определения фигуры.')
        items.append(rectangle_feat_3)
        rectangle_feat_4 = Feature(text='Диагональ прямоугольника разбивает фигуру на два малых равных прямоугольных треугольника. Это свойство легко доказать. Треугольники будут прямоугольными, так как включают в себя по одному углу в 90 градусов. При этом диагональ будет являться общей стороной, а катеты окажутся равными, так как противоположные стороны параллелограмма попарно равны и параллельны.')
        items.append(rectangle_feat_4)
        rectangle_feat_5 = Feature(text='Диагонали прямоугольника равны.')
        items.append(rectangle_feat_5)
        rectangle = Figure(name='Прямоугольник',
                           info='Прямоугольник — это параллелограмм, у которого все углы равны 90 градусам. У прямоугольника всего три основных признака: \n 1)По углу. Если один из углов параллелограмма равен 90 градусам, то параллелограмм является прямоугольником. \n  2)Если три угла четырехугольника равны 90 градусам, то такой четырехугольник является прямоугольником. Обратите внимание, что в этом случае нет необходимости доказывать, что перед нами параллелограмм. Достаточно знать значения углов четырехугольника. \n  3)По диагоналям: если диагонали параллелограмма равны, то такой параллелограмм является прямоугольником.',
                           image='http://www.zoograeber.de/wp-content/uploads/bilder/seiten/aquaristik/a-a-s-standard.jpg',
                           plain=True,
                           features=[rectangle_feat_1,rectangle_feat_2,rectangle_feat_3,rectangle_feat_4,rectangle_feat_5])
        items.append(rectangle)

        #Окружность
        formula_d_circle = Formula(name='Диаметр окружности', description='Диаметр равен удвоенному радиусу окружности. Радиус - расстояние от центра до любой точки окружности. Обозначается латинской R.',
                                      latex=self.latex_formula('d = 2 R = \\frac{C}{\pi}'))
        items.append(formula_d_circle)
        formula_dl_circle = Formula(name='Длина окружности', description='Длина окружности – это общая длина границы круга. В математике длину окружности обозначают латинскими буквами C или L.',
                                      latex=self.latex_formula('C = 2 \pi R=\pi d'))
        items.append(formula_dl_circle)
        formula_s_circle = Formula(name='Площадь окружности', description='Площадь круга — величина, определяющая размеры плоскости, ограниченной какой-либо окружностью. ',
                                latex=self.latex_formula('S = \pi R^{2}'))
        items.append(formula_s_circle)
        circle_feat_1 = Feature(text='Кратчайшее расстояние от центра окружности к секущей (хорде) всегда меньше радиуса.')
        items.append(circle_feat_1)
        circle_feat_2 = Feature(text='Через три точки, которые не лежат на одной прямым, можно провести только одну окружность.')
        items.append(circle_feat_2)
        circle_feat_3 = Feature(text='Среди всех замкнутых кривых с одинаковой длиной, окружность имеет наибольшую площадь.')
        items.append(circle_feat_3)
        circle_feat_4 = Feature(text='Если две окружности соприкасаются в одной точке, то эта точка лежит на прямой, что проходит через центры этих окружностей.')
        items.append(circle_feat_4)
        circle = Figure(name='Окружность',
                     info='Окружность — это совокупность всех точек на плоскости, которые находятся на одинаковом расстоянии от заданной точки О, которая называется центром окружности.Элементы окружности: \n радиус, диаметр, хорда, дуга. \n Вся дуга окружности имеет градусную меру 360 градусов. Половина дуги окружности равна 180 градусам.',
                     image='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Circle_with_radius_and_diameter.png/240px-Circle_with_radius_and_diameter.png',
                     plain=True,
                     features=[circle_feat_1,circle_feat_2,circle_feat_3,circle_feat_4])
        items.append(circle)
        #Трапеция
        formula_m_trapezoid = Formula(name='Средняя линия трапеции', description='Средняя линия трапеции — это отрезок, который соединяет середины боковых сторон трапеции. ',
                                   latex=self.latex_formula('m = \\frac{a + b}{2}'))
        items.append(formula_m_trapezoid)
        formula_s_trapezoid = Formula(name='Площадь трапеции', description='Чтобы найти площадь трапеции необходимо найти высоту, умножить её на полусумму оснований. ',
                                      latex=self.latex_formula('S = \\frac{a + b}{2} h'))
        items.append(formula_s_trapezoid)
        trapezoid_feat_1 = Feature(text='Сумма углов трапеции, прилежащих к одной и той же боковой стороне, равна 180°.')
        items.append(trapezoid_feat_1)
        trapezoid_feat_2 = Feature(text='Средняя линия трапеции параллельна ее основаниям и равняется половине их суммы.')
        items.append(trapezoid_feat_2)
        trapezoid_feat_3 = Feature(text='Отрезок, который соединяет середины диагоналей трапеции, лежит на ее средней линии и равняется половине разности оснований.')
        items.append(trapezoid_feat_3)
        trapezoid_feat_4 = Feature(text='Точки пересечения диагоналей трапеции, продолжений ее боковых сторон и середин оснований лежат на одной прямой.')
        items.append(trapezoid_feat_4)
        trapezoid_feat_5 = Feature(text='Диагонали трапеции делят ее на 4 треугольника, два из которых (при основаниях) подобны, а два других (при боковых сторонах) равны по площади.')
        items.append(trapezoid_feat_5)
        trapezoid_feat_6 = Feature(text='Биссектрисы углов трапеции при одинаковой боковой стороне взаимно перпендикулярны.')
        items.append(trapezoid_feat_6)
        trapezoid_feat_7 = Feature(text='В трапецию можно вписать окружность только в том случае, если сумма длин ее оснований равна сумме длин ее боковых сторон.')
        items.append(trapezoid_feat_7)
        trapezoid = Figure(name='Трапеция',
                           info='Трапеция – это четырехугольник, две стороны которого параллельны, а остальные две – нет.Все трапеции можно разделить на три вида: \n 1— равнобедренные трапеции; \n 2— прямоугольные трапеции; \n 3— произвольные трапеции.',
                           image='https://topuch.com/mektep-izilorda-alasi-i-altinsarin-atindai-10-mektep-liceji/826526_html_cf145c709ea7cce8.jpg',
                           plain=True,
                           features=[trapezoid_feat_1,trapezoid_feat_2,trapezoid_feat_3,trapezoid_feat_4,trapezoid_feat_5,trapezoid_feat_6,trapezoid_feat_7])
        items.append(trapezoid)
        #Треугольник
        formula_s_triangle = Formula(name='Площадь треугольника', description='Площадь треугольника – численная характеристика, из которой мы узнаем о размере части плоскости, ограниченной данной фигурой.',
                                      latex=self.latex_formula('S = \\frac{1}{2} h a'))
        items.append(formula_s_triangle)
        triangle_feat_1 = Feature(text='Больший угол всегда лежит напротив большей стороны.')
        items.append(triangle_feat_1)
        triangle_feat_2 = Feature(text='Равные углы всегда лежат напротив равных сторон.')
        items.append(triangle_feat_2)
        triangle_feat_3 = Feature(text='Совокупность углов в данной фигуре всегда будет равна 180 градусам.')
        items.append(triangle_feat_3)
        triangle_feat_4 = Feature(text='Любая сторона фигуры будет меньше совокупности двух других сторон, а также больше разности этих сторон. Пример: AB + BC > AC.')
        items.append(triangle_feat_4)
        triangle_feat_5 = Feature(text='По свойствам углов выделяют три вида треугольников:Остроугольный - Все его углы являются острыми.Прямоугольный - Только один угол является прямым (то есть, он равен 90 градусам).Тупоугольный - Один угол является тупым.')
        items.append(triangle_feat_5)
        triangle = Figure (name='Треугольник',
                           info='Треугольник — геометрическая фигура, образующаяся в случае соединения трех отрезков с тремя точками, которые не лежат на одной прямой. Вершинами треугольника называют три точки, которые соединяются отрезками, а отрезки называют сторонами.Виды треугольников: \n  Остроугольный, \n Тупоугольный, \n Прямоугольный, \n Разносторонний, \n Равнобедренный, \n Равносторонний',
                           image='https://ru-static.z-dn.net/files/d7c/83d7c97bf05bfc33c7a718dbaea76522.gif',
                           plain=True,
                           features=[triangle_feat_1,triangle_feat_2,triangle_feat_3,triangle_feat_4,triangle_feat_5])
        items.append(triangle)
        #Ромб
        formula_s_rhomb = Formula(name='Площадь ромба', description='Площадь ромба равна половине произведения его диагоналей.',
                                     latex=self.latex_formula('S = \\frac{d_{1} d_{2}}{2} = h a'))
        items.append(formula_s_rhomb)
        formula_p_rhomb = Formula(name='Периметр ромба', description='Периметр (P) ромба равняется сумме длин всех его сторон. ',
                                  latex=self.latex_formula('P = 4a'))
        items.append(formula_p_rhomb)
        rhomb_feat_1 = Feature(text='Диагонали ромба пересекаются под прямым углом.')
        items.append(rhomb_feat_1)
        rhomb_feat_2 = Feature(text='Диагонали ромба являются его биссектрисами.')
        items.append(rhomb_feat_2)
        rhomb_feat_3 = Feature(text='Сумма квадратов диагоналей равен четырем квадратом стороны.')
        items.append(rhomb_feat_3)
        rhomb = Figure (name='Ромб',
                        info='Ромб — четырехугольник (параллелограмм), у которого все стороны равны.Признаки ромба: \n 1-Если у параллелограмма диагонали взаимно перпендикулярны, то он является ромбом  \n 2-Если диагональ параллелограмма является биссектрисой его углов, то он является ромбом \n 3-Если у четырехугольника все стороны равны, то он является ромбом ',
                        image='https://www.learncram.com/wp-content/uploads/2019/08/Maharashtra-Board-Class-8-Maths-Solutions-Chapter-15-Area-Practice-Set-15.2-2.png',
                        plain=True,
                        features=[rhomb_feat_1,rhomb_feat_2,rhomb_feat_3])
        items.append(rhomb)
        #Окружность
        formula_s_sphere = Formula(name='Площадь поверхности шара', description='Где S-площадь, R-радиус шара',
                                  latex=self.latex_formula('S = 4 \pi R^{2}'))
        items.append(formula_s_sphere)
        formula_v_sphere = Formula(name='Объём шара', description='Как и все трехмерные тела, шар обладает несколькими специфическими параметрами. Один из них объем – вместимость пространства, которое он занимает. Переводя на язык материальных объектов, это количество воздуха, воды или любого другого вещества, которое поместится внутрь ограничивающей шар сферы.',
                                   latex=self.latex_formula('V = \\frac{4}{3} \pi R^{3}'))
        items.append(formula_v_sphere)
        sphere_feat_1 = Feature(text='Любое сечение шара плоскостью является кругом.')
        items.append(sphere_feat_1)
        sphere_feat_2 = Feature(text='Любое сечение сферы плоскостью является окружностью.')
        items.append(sphere_feat_2)
        sphere_feat_3 = Feature(text='Все точки сферы равноудалены от ее центра.')
        items.append(sphere_feat_3)
        sphere_feat_4 = Feature(text='Сфера имеет самый большой объем среди всех фигур в пространстве, имеющих одинаковую площадь поверхности.')
        items.append(sphere_feat_4)
        sphere_feat_5 = Feature(text='Через две любые диаметрально противоположные точки (максимально отдаленные друг от друга точки на окружности) можно провести неограниченное количество кругов для шара или окружностей для сфер радиусом, равным радиусу шара/сферы.')
        items.append(sphere_feat_5)
        sphere = Figure (name='Сфера',
                         info='Сфера – это поверхность шара. Образуется путем вращения окружности вокруг своего диаметра на 180° или полуокружности – на 360°.',
                         image='sphere',
                         plain=False,
                         features=[sphere_feat_1,sphere_feat_2,sphere_feat_3,sphere_feat_4,sphere_feat_5])
        items.append(sphere)

        #Икосаэдр
        formula_p_icos = Formula(name='Сумма длин рёбер', description='Икосаэдр имеет 30 равных ребер, следовательно, сумма всех длин ребер или периметр икосаэдра равен произведению длины одного ребра на 30 (их общее количество). В формуле, a - длина ребра икосаэдра. ',
                                   latex=self.latex_formula('P = 30a'))
        items.append(formula_p_icos)
        formula_v_icos = Formula(name='Объем икосаэдра', description='Где a  – длина ребра икосаэдра.',
                                 latex=self.latex_formula('V = \\frac{5}{12} ( 3 + \sqrt{5}) a^{2}'))
        items.append(formula_v_icos)
        formula_s_icos = Formula(name='Площадь икосаэдра', description='Икосаэдр составлен из двадцати равносторонних треугольников. Фигура имеет 20 граней, 12 вершин и 30 рёбер.',
                                 latex=self.latex_formula('S = 5 a^{2} \sqrt{3}'))
        items.append(formula_s_icos)
        formula_ro_icos = Formula(name='Радиус описанной вокруг икосаэдра сферы', description='Икосаэдр может быть помещен в сферу (вписан), так, что каждая из его вершин будет касаться внутренней стенки сферы.',
                                 latex=self.latex_formula('R = \\frac{1}{4} \sqrt{2 ( 5 + \sqrt{5}) a}'))
        items.append(formula_ro_icos)
        formula_rv_icos = Formula(name='Радиус вписанной в икосаэдр сферы', description='Сфера может быть вписана внутрь икосаэдра.',
                                  latex=self.latex_formula('R = \\frac{1}{4 \sqrt{3}} (3 + \sqrt{5}) a'))
        items.append(formula_rv_icos)
        icos_feat_1 = Feature(text='Каждая из 12 вершин икосаэдра лежит по 3 в 4-х параллельных плоскостях, образуя во всех плоскостях правильный треугольник.')
        items.append(icos_feat_1)
        icos_feat_2 = Feature(text='10 вершин икосаэдра находятся в 2-х параллельных плоскостях, и образуют в них 2 правильных 5-ти угольника, а оставшиеся 2 — противоположны друг другу и находятся в 2-х концах диаметра описанной вокруг икосаэдра сферы, который перпендикулярен параллельным плоскостям.')
        items.append(icos_feat_2)
        icos_feat_3 = Feature(text='Икосаэдр возможно вписать в куб, тогда 6 взаимо-перпендикулярных ребер икосаэдра будут находиться соответственно на 6-ти гранях куба, оставшиеся 24 ребра находятся внутри куба, все 12 вершин икосаэдра будут находиться на ше6-ти гранях куба.')
        items.append(icos_feat_3)
        icos_feat_4 = Feature(text='В икосаэдр можно вписать тетраэдр, таким образом, чтобы 4 вершины тетраэдра станут совмещены с 4-мя вершинами икосаэдра.')
        items.append(icos_feat_4)
        icos_feat_5 = Feature(text='Икосаэдр возможно вписать в додекаэдр, тогда вершины икосаэдра совместятся с центрами граней додекаэдра.')
        items.append(icos_feat_5)
        icos_feat_6 = Feature(text='В икосаэдр возможно вписать додекаэдр с совмещением вершин додекаэдра и центров граней икосаэдра.')
        items.append(icos_feat_6)
        icos_feat_7 = Feature(text='Усечённый икосаэдр можнополучить, срезав 12 вершин с образованием граней вида правильных 5-ти угольников. Тогда количество вершин нового многогранника увеличится в 5 раз (12×5=60), 20 треугольных граней становятся правильными шестиугольниками (количество граней теперь 20+12=32), а рёбер - 30+12×5=90.')
        items.append(icos_feat_7)
        icos_feat_8 = Feature(text='Сделать икосаэдра можно из 20 тетраэдров.')
        items.append(icos_feat_8)
        icos_feat_9 = Feature(text='Нельзя сделать икосаэдр из правильных тетраэдров, потому что радиус описанной сферы вокруг икосаэдра и длина бокового ребра (вершины-центр такой сборки) тетраэдра меньше ребра икосаэдра.')
        items.append(icos_feat_9)
        icos = Figure(name='Икосаэдр',
                      info='Икосаэдр — правильный выпуклый многогранник, двадцатигранник, один из тел Платона.',
                      image='icos',
                      plain=False,
                      features=[icos_feat_1,icos_feat_2,icos_feat_3,icos_feat_4,icos_feat_5,icos_feat_6,icos_feat_7,icos_feat_8,icos_feat_9])
        items.append(icos)
        #Пирамида
        formula_sb_pyro = Formula(name='Площадь боковой стороны пирамиды', description='Чтобы вычислить площадь боковой поверхности пирамиды, необходимо знать длины боковых рёбер и периметр основания.',
                                 latex=self.latex_formula('S = \\frac{P_{основания} h_{a}} {2}'))
        items.append(formula_sb_pyro)
        formula_v_pyro = Formula(name='Обьем пирамиды', description='Чтобы рассчитать объем пирамиды, вам нужно знать ее высоту и площадь основания. Получив эту информацию, вы можете определить объем',
                                  latex=self.latex_formula('V = \\frac{1}{3} S_{основания} h'))
        items.append(formula_v_pyro)
        pyro_feat_1 = Feature(text='Все боковые ребра фигуры равны. Другими словами вершина пирамиды находится на одинаковом расстоянии от всех углов ее основания.')
        items.append(pyro_feat_1)
        pyro_feat_2 = Feature(text='Угол между всеми боковыми ребрами и основанием одинаковый')
        items.append(pyro_feat_2)
        pyro_feat_3 = Feature(text='Все грани наклонены к основанию под одним и тем же углом.')
        items.append(pyro_feat_3)
        pyro_feat_4 = Feature(text='Площади всех боковых граней равны.')
        items.append(pyro_feat_4)
        pyro_feat_5 = Feature(text='Все апофемы равны.')
        items.append(pyro_feat_5)
        pyro_feat_6 = Feature(text='Вокруг пирамиды можно описать сферу, центром которой будет точка пересечения перпендикуляров, проведенных к серединам боковых ребер.')
        items.append(pyro_feat_6)
        pyro_feat_7 = Feature(text='В пирамиду можно вписать сферу, центром которой будет точка пересечения биссектрис, берущих начало в углах между боковыми ребрами и основанием фигуры.')
        items.append(pyro_feat_7)
        pyro = Figure(name='Пирамида',
                      info='Пирамида – это геометрическая фигура в пространстве; многогранник, который состоит из основания и боковых граней (с общей вершиной), количество которых зависит от количества углов основания.',
                      image='pyro',
                      plain=False,
                      features=[pyro_feat_1,pyro_feat_2,pyro_feat_3,pyro_feat_4,pyro_feat_5,pyro_feat_6,pyro_feat_7])
        items.append(pyro)

        #Конус
        formula_sb_cone = Formula(name='Площадь боковой поверхности конуса', description='Площадь боковой поверхности конуса равна произведению его радиуса и образующей умноженному на число π.',
                                  latex=self.latex_formula('S = \pi r l'))
        items.append(formula_sb_cone)
        formula_s_cone = Formula(name='Площадь полной поверхности конуса', description='Наряду с площадью боковой поверхности можно найти и площадь полной поверхности. Для этого к площади боковой поверхности надо прибавить площадь основания. ',
                                  latex=self.latex_formula('S = \pi r (l + r)'))
        items.append(formula_s_cone)
        formula_v_cone = Formula(name='Обьём конуса', description='Объем конуса — это пространство, занимаемое всеми частями конуса внутри его ограничивающих плоскостей. ',
                                 latex=self.latex_formula('V = \\frac{1}{3} \pi r^{2} h'))
        items.append(formula_v_cone)
        cone_feat_1 = Feature(text='Все образующие конуса имеют одинаковую длину.')
        items.append(cone_feat_1)
        cone_feat_2 = Feature(text='Конус образуется путем вращения прямоугольного треугольника вокруг одного из катетов на 360° или равнобедренного треугольника (состоит из двух равных прямоугольных треугольников) вокруг своей оси на 180°.')
        items.append(cone_feat_2)
        cone_feat_3 = Feature(text='При пересечении конуса любой плоскостью, параллельной его основанию, получается круг (коническое сечение). Образованная между основанием и данным кругом фигура – это усеченный конус.')
        items.append(cone_feat_3)
        cone_feat_4 = Feature(text=' Если секущая плоскость не параллельна основанию конуса, то результатом сечения является эллипс.')
        items.append(cone_feat_4)
        cone_feat_5 = Feature(text='Если секущая плоскость проходит через основание конуса, то результатом сечения является парабола/гипербола.')
        items.append(cone_feat_5)
        cone_feat_6 = Feature(text='Результатом сечения конуса плоскостью, проходящей через его ось (или высоту), является равнобедренный треугольник.')
        items.append(cone_feat_6)
        cone_feat_7 = Feature(text='Центр тяжести конуса расположен на четверти его высоты, считая от основания.')
        items.append(cone_feat_7)
        cone = Figure(name='Конус',
                      info='Конус — это тело, получающееся при вращении прямоугольного треугольника вокруг прямой, содержащей один из его катетов.',
                      image='cone',
                      plain=False,
                      features=[cone_feat_1,cone_feat_2,cone_feat_3,cone_feat_4,cone_feat_5,cone_feat_6,cone_feat_7])
        items.append(cone)





























































        # Теорема Пифагора

        formula_pifa = Formula(name='Формула Пифагора', description='Теоре́ма Пифаго́ра — одна из основополагающих теорем евклидовой геометрии, устанавливающая соотношение между сторонами прямоугольного треугольника: сумма квадратов длин катетов равна квадрату длины гипотенузы.', latex=self.latex_formula('c^2 = a^2 + b^2'))
        items.append(formula_pifa)

        theorema = Theorema(name='Теорема Пифагора', text='Теоре́ма Пифаго́ра — одна из основополагающих теорем евклидовой геометрии, устанавливающая соотношение между сторонами прямоугольного треугольника: сумма квадратов длин катетов равна квадрату длины гипотенузы. Основные направления доказательств: алгебраическое использование соотношений элементов треугольника (таков, например, популярный метод подобия), метод площадей, существуют также различные экзотические доказательства (например, с помощью дифференциальных уравнений).',
                            formulas=[formula_pifa])
        items.append(theorema)

        # Теорема о равенстве треугольников
        theorema_2 = Theorema(name='Теорема о равенстве треугольников', text='Если две стороны и угол между ними одного треугольника соответственно равны двум сторонам и углу между ними другого треугольника, то такие треугольники равны.')
        items.append(theorema_2)
        # Теорема о сумме углов треугольника
        theorema_3 = Theorema(name='Теорема о сумме углов треугольника', text='Сумма углов в треугольнике всегда равна 180 градусам.')
        items.append(theorema_3)
        #Теорема о равенстве треугольников
        theorema_4 = Theorema(name='Теорема о равенстве треугольников', text='Два треугольника равны, если у них одинаковые три стороны или если у них равны две стороны и угол между ними.')
        items.append(theorema_4)
        #Свойство суммы углов четырехугольника
        theorema_5 = Theorema(name='Свойство суммы углов четырехугольника', text='Сумма внутренних углов в четырехугольнике всегда равна 360 градусам.')
        items.append(theorema_5)
        #Теоремы о параллельных прямых
        theorema_6 = Theorema(name='Теоремы о параллельных прямых', text='Если две параллельные прямые пересечены секущей, то соответственные углы равны. Если две параллельные прямые пересечены секущей, то сумма односторонних углов равна 180°. Если при пересечении двух прямых секущей накрест лежащие углы равны, то прямые параллельны.')
        items.append(theorema_6)
        #Теорема косинусов
        formula_cos = Formula(name='Теорема косинусов', description='Квадрат стороны треугольника равен сумме квадратов двух других его сторон минус удвоенное произведение этих сторон, умноженное на косинус угла между ними', latex=self.latex_formula('a^{2} = b^{2} + c^{2} - 2 b c cosA'))
        items.append(formula_cos)

        theorema_7 = Theorema(name='Теорема косинусов', text='Квадрат стороны треугольника равен сумме квадратов двух других его сторон минус удвоенное произведение этих сторон на косинус угла между ними.',
                              formulas=[formula_cos])
        items.append(theorema_7)
        #Теорема синусов
        formula_sin = Formula(name='Теорема синусов', description='Теорема синуса, также известная как закон синусов, представляет собой тригонометрическую формулу, используемую для решения треугольников. Он гласит, что отношение длины стороны треугольника к синусу угла, противоположного этой стороне, одинаково для всех трех сторон. Другими словами, отношение длины стороны к синусу противоположного ей угла является постоянной величиной.', latex=self.latex_formula('\\frac{a}{sinA} = \\frac{b}{sinB} = \\frac{c}{sinC} =2 R'))
        items.append(formula_sin)
        theorema_8 = Theorema(name='Теорема синусов', text='Отношение длины стороны треугольника к синусу противолежащего угла равно двум радиусам описанной около треугольника окружности.',
                              formulas=[formula_sin])
        items.append(theorema_8)


        print("BD load finish")
        return items
